from django import forms
from .views import get_available_account_names


class environment_choice_form(forms.Form):

    cloud_account_name = ''
    radio_button = ''
    radio_buttons_list = []
    radio_button_id = ''
    radio_button_name = ''

    for cloud_account_name in get_available_account_names():
        radio_button_id = cloud_account_name
        radio_button_name = cloud_account_name
        radio_button = (radio_button_id, radio_button_name)

        radio_buttons_list.append(radio_button)

    cloud_accounts = forms.ChoiceField(widget=forms.RadioSelect(),
                                       choices=radio_buttons_list)
