import logging
import sys

from django.shortcuts import render

from backend.views import CloudReader, get_available_account_names
from .elapsed_time_counter import ElapsedTime
from .http_request_parser import get_client_ip
from .forms import environment_choice_form
from .models_django_tables2 import (
    table_model_compute_info, table_model_database_info, table_model_dns_info,
    table_model_loadbalancing_info, table_model_objectstore_info
)
from .time_to_string_converter import TimeConverter


logging.basicConfig(level="INFO")
log = logging.getLogger(__name__)


def homepage(request):

    timer = ElapsedTime()
    timer.start_counting()

    log.info("HTTP request came from ip: %s", get_client_ip(request))

    raw_compute_info = []
    raw_loadbalancing_info = []
    raw_database_info = []
    raw_dns_info = []
    raw_objectstore_info = []

    target_cloud_account_name = ""

    messages = []

    if request.method == 'POST':
        form = environment_choice_form(request.POST)

        if form.is_valid():
            target_cloud_account_name = form.cleaned_data.get("cloud_accounts")

            message_text = "Problem occurred when querying {} account ".format(target_cloud_account_name)

            cloud_assets = CloudReader(target_cloud_account_name)

            try:
                raw_compute_info = cloud_assets.get_compute_info()
            except Exception:
                log.exception(sys.exc_info()[0])
                messages.append(message_text + ". EC2 info")

            try:
                raw_loadbalancing_info = cloud_assets.get_loadbalancing_info()
            except Exception:
                log.exception(sys.exc_info()[0])
                messages.append(message_text + ". ELB info")

            try:
                raw_database_info = cloud_assets.get_database_info()
            except Exception:
                log.exception(sys.exc_info()[0])
                messages.append(message_text + ". RDS info")

            try:
                raw_dns_info = cloud_assets.get_dns_info()
            except Exception:
                log.exception(sys.exc_info()[0])
                messages.append(message_text + ". Route53 info")

            try:
                raw_objectstore_info = cloud_assets.get_objectstore_info()
            except Exception:
                log.exception(sys.exc_info()[0])
                messages.append(message_text + ". S3 info")
    else:
        form = environment_choice_form()

    radio_buttons = form

    if len(radio_buttons.radio_buttons_list) == 0:
        messages.append("No accounts found in configuration file")

    table_compute_details = table_model_compute_info(raw_compute_info)
    table_loadbalancing_details = table_model_loadbalancing_info(raw_loadbalancing_info)
    table_database_details = table_model_database_info(raw_database_info)
    table_dns_details = table_model_dns_info(raw_dns_info)
    table_objectstore_details = table_model_objectstore_info(raw_objectstore_info)

    timer.stop_counting()
    time_elapsed_seconds = timer.get_seconds()

    log.info("Query took: %s second(-s)", time_elapsed_seconds)

    return render(request, 'index.html', {
        'form_choose_environment': radio_buttons,
        'target_cloud_account_name': target_cloud_account_name,
        'error_messages': messages,
        'table_compute_details': table_compute_details,
        'table_database_details': table_database_details,
        'table_dns_details': table_dns_details,
        'table_loadbalancing_details': table_loadbalancing_details,
        'table_objectstore_details': table_objectstore_details,
        'time_elapsed_seconds': time_elapsed_seconds,
        'string_last_used': TimeConverter.get_last_usage_string()
    })
