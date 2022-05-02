# nebula3_experts
## Base module for all experts

## HOW TO USE THIS REPO from VSCODE:
1. `git clone https://github.com/NEBULA3PR0JECT/nebula3_experts.git --recursive`

## HOW TO USE THIS REPO with DOCKER:
First, clone this repo:
1. `git clone https://github.com/NEBULA3PR0JECT/nebula3_experts.git --recursive`

For GPU usage (recommended):

2. `cd nebula3_experts && cd Docker && cd microservice-gpu`

For CPU usage (not recommended, unless you're 100% sure you don't need gpu):

2. `cd nebula3_experts && cd Docker && cd microservice-cpu`

Build the docker:

3. docker build -t microservice-expert .

*Note:* You can change `microservice-expert` to your desired image name.

Run the docker (with GPU):

4. `docker run -it -p 8088:8088 --gpus all microservice-expert:latest`

Run the docker (with CPU):

4. `docker run -it -p 8088:8088 microservice-expert:latest`


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

