import django_tables2 as tables


class table_model_compute_info(tables.Table):
    InstanceId = tables.Column()
    name = tables.Column(order_by="name")
    autoscaling_group_name = tables.Column()
    PrivateIpAddress = tables.Column()
    LaunchTime = tables.Column()

    class Meta:
        attrs = {'class': 'table table-hover'}
        order_by = "name"


class table_model_database_info(tables.Table):
    DatabaseName = tables.Column()
    DatabaseStatus = tables.Column()
    DatabaseAddress = tables.Column()
    DatabaseCreateTime = tables.Column()
    Engine = tables.Column()
    EngineVersion = tables.Column()

    class Meta:
        attrs = {'class': 'table table-hover'}


class table_model_dns_info(tables.Table):
    Name = tables.Column(order_by="Name")
    Type = tables.Column()
    Target = tables.Column(empty_values=())

    def render_target(self, value, record):
        string = ",".join(record['Target'])
        return string

    class Meta:
        attrs = {'class': 'table table-hover'}
        order_by = "Name"

class table_model_loadbalancing_info(tables.Table):
    LoadBalancerName = tables.Column(order_by="LoadBalancerName")
    DNSName = tables.Column()
    Type = tables.Column()
    Scheme = tables.Column()

    class Meta:
        attrs = {'class': 'table table-hover'}
        order_by = "LoadBalancerName"


class table_model_objectstore_info(tables.Table):
    Name = tables.Column(order_by="Name")
    CreationDate = tables.Column()

    class Meta:
        attrs = {'class': 'table table-hover'}
        order_by = "Name"
