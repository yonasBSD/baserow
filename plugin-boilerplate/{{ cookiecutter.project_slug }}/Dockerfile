FROM baserow/baserow:1.34.5

COPY ./plugins/{{ cookiecutter.project_module }}/ /baserow/plugins/{{ cookiecutter.project_module }}/
RUN /baserow/plugins/install_plugin.sh --folder /baserow/plugins/{{ cookiecutter.project_module }}
