# nebula3_experts
## Base module for all experts

## HOW TO USE THIS REPO:
1. `git clone https://github.com/NEBULA3PR0JECT/nebula3_experts.git --recursive`

## Expert Configuration
- Since experts are started in a microservice container (via gradient or else), it is useless to
  set configuration in the command args, therefore, expert's specific configuration
  (model type, model tune params etc) should come from env.
  Further info can be found in: https://12factor.net/config
- every expert can have something similar to ExpertsConf class like NEBULA_CONF

## CLI
- CLI is now done via the REST api, each expert microservice app has a web server with
  all the apis documented via the /docs (or /redoc) url, which also provide a basic way
  to operate the experts api.
- Postman and other apps can be used to operate the apis
- If you still want to work from terminal, learn curl.

#
- when an expert starts a new taks it has to call self.add_task and when finishes call self.remove_task
- since expert is running in container, all the logs are going to stdout/stderr so that they could be
  seen from outside using docker logs, and that we can aggragate them





# todo:
- add get/set logger level

