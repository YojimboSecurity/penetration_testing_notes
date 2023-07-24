---
Client: {{ cookiecutter.client_name }}
App: {{ cookiecutter.app_name }}
Created: {{ cookiecutter.testing_date }}
---

{% if cookiecutter.engagement_type  == 'web_app'  %}
    {% set ip = cookiecutter.ip %}
    {% include "notes.md" %}
{% elif cookiecutter.engagement_type == 'network' %}
    {% set network = cookiecutter.network %}
## Network base: {{ network.base }}
## Network sets: {{ network.sets }}
    {% for i in network.sets %}
        {% set ip = network.base+'.'+i|string %}
        {% include "notes.md" %}
    {% endfor %}
{% endif %}
