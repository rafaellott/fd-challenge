# FD Challenge


---
**NOTE**

In the Postman Collection, the provided BearerToken is invalid.
See section [How to asdf the token?](#how-to-generate-the-token?)

---

## How to run the app?

The application was Dockerized. To run it, you need first to build the image 
then create a container from that built image

### Build:
- In root folder, run the following command:

    `$ docker build . -t fd-app`


### Run
- In root folder, run the following command:

    `$ docker run -p 8080:8080 --rm fd-app:latest`

### Extra options
- You can change the Data Fetch URL. To do it, run the container 
passing a valid URL to the ENV VAR named `FETCH_URL`. Example below:
  
    `$ docker run -p 8080:8080 -e FETCH_URL=<URL_TO_FETCH_DATA> --rm fd-app:latest`

## How to generate the token?

- Go to [https://jwt.io](https://jwt.io)
- On **PAYLOAD**, create a dict with key `username` and value `frameworkdigital`.
- On **VERIFY SIGNATURE**, change value from `your-256-bit-secret` to `secret_word`.
This is not safe, ideally this content should go to ENV VAR.
- Copy the JWT generated on **ENCODED** field.
- Add in the **Header** the `Authorization: Bearer <THE-GENERATED-JWT>` 


## How to execute the tests?

- In root folder, create the pipenv environment with development libraries, executing the following command: `$ pipenv install --dev`
- After completion, go to folder **src** `$ cd src/`
- To run the tests, execute command: `$pytest tests/`
