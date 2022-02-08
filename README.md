<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Cloud function Template</h3>

  <p align="center">
    Short definition
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#test">Test</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#deploy">Deployment</a></li>
    <li><a href="#folder-organization">Folder Organization</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project 🤔

LONG PROJECT DESCRIPTION

There are many great README templates available on GitHub, however, I didn't find one that really suit my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have have contributed to expanding this template!

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With 🧰

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python 3.8](https://www.python.org/downloads/release/python-385/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)


<!-- GETTING STARTED -->
## Getting Started 🚀

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites ✔️

This is an example of how to list things you need to use the software and how to install them.

* You need to setup your GCP Account into your local machine. Follow [documentation](https://cloud.google.com/sdk/docs/install)

* pyenv

  ```sh
  brew install pyenv
  ```

* Create virtual environment

  ```sh
  pyenv virtualenv 3.8.5 my-env
  ```

* Activate virtual environment

  ```sh
  pyenv activate my-env
  ```

* Environment variables required
  - DB_URL: Database URL
  - SENTRY: Sentry URL
  - LEVEL: Debug Level

### Installation 💻

Steps to run app

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/urbvan/Project-Name.git
   ```
3. Install project dependencies
   ```sh
   pip install -r requirements.txt
   ```



<!-- USAGE EXAMPLES -->
## Usage 🏃

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation (API Documentation)](https://example.com)_

## Test ✅

Use this space to show us how to run your application tests. Example:

```
pytest <folder>
```

## Deploy:flying_saucer:

Use [Makefile](Makefile) and change settings inside makefile to deploy your function to GCP. If you need other options please follow  [GCP Cloud function documentation](https://cloud.google.com/functions/docs/quickstart-python)


```Example
make deploy-pubsub
```

<!-- FOLDER ORGANIZATION -->
## Folder Organization 📁

- src: Source project
- main.py: This file receives request from GCP Cloud Function URL


Make with ❤️ by Urbvan
