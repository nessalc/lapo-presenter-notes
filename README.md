# Lake Afton Public Observatory Presenter Notes

This project uses [MKDocs](http://www.mkdocs.org/) to create web pages providing notes of the objects and programs used at the telescope during the public programs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [Build and Deployment](#build-and-deployment) below for notes on how to deploy the project on a live system.

## Build Environment

This project was built using the following environment components:

[Visual Studio Code](https://code.visualstudio.com/)

[Git for Windows](https://git-scm.com/download/win)

[Python 3.11.2](https://www.python.org/downloads/)

## Project Setup

The following are the steps I used to create the fresh Presenter Notes project,
and these notes can be used for creating a fresh, brand-new MkDocs project.
However, if you are just cloning the existing Presenter Notes project from GitHub, then you can skip these steps and go directly to [Clone this Project](#clone-this-project)
 	
### Virtual Environment

Create a virtual environment for the Presenter Notes Project.  
Begin by creating a directory for the Python virtual environment;

Example... from within your lake-afton-presenter-notes project folder

```bat
py -m venv venv
```

#### Activate the virtual environment

You can do this from any folder location, recommend from your local github\lake-afton-presenter-notes project folder

```bat
.\venv\Scripts\activate.bat
```

## Prerequisites

See the pip-dependencies.txt file for the Python package requirements for the LAPO Presenter Notes:

### Install Python Packages

**Short-cut**: to install *ALL* pip dependencies:
The following *must* be done from your local github\lake-afton-presenter-notes project folder, where the pip-dependencies.txt exists...

```bat
pip install -r pip-dependencies.txt --use-pep517
```

For manual installation, do the following:

From your project folder, install MKDocs:

```bat
pip install mkdocs
```

reference [MKDocs](http://www.mkdocs.org/) for more information

Theme:
This project uses the MkDocs Bootswatch Theme: [Cyborg](http://mkdocs.github.io/mkdocs-bootswatch/#cyborg)

```bat
pip install mkdocs-bootswatch
```

### Distance Data

Javascripts have been added to the project, see docs\js\utils.js and docs\init\initialize-json.py, both of these work to create and update ***current*** distance information for each object within the Solar System on pages for each Solar System object. Once the site is up, visit [The Moon > Overview](http://localhost:8000/solar-system/moon/) for example.

Before starting up the MKDocs server, initialize the Distance Data file with the following command:

```bat
py .\docs\init\initialize_json.py
```

### Start MkDocs Server - for local testing

To start the MKDocs dev server for testing.
From the presenterNotes folder, execute the following command

```bat
mkdocs serve
```

You can then open the local site for testing:<br/>

```txt
http://127.0.0.1:8000/
```

## Clone this Project

From the [GitHub repository](https://github.com/caketron/lake-afton-presenter-notes),
select "Code" and copy the URL to the repo, e.g.: <https://github.com/caketron/lake-afton-presenter-notes.git>

Then from your local project folder (I am using c:\git\github), execute the following git command:

```bat
git clone https://github.com/caketron/lake-afton-presenter-notes
```

## Build and Deployment

Once all editing has been completed, do a final build of the document site for deployment

```bat
mkdocs build
```

This command will generate the various pages from the markdown files and place them in the "site" sub-directory.

You can use the Python Simple HTTP server that comes with Python to start up a local server.
Change directory into the Site folder and execute the following:

```bat
py -m http.server 8080
```

Then visit the site by visiting the following address in your browser:

[http://127.0.0.1:8080/](http://127.0.0.1:8080/)

## Simplified Deployment

Once the build has completed, a **Site** folder will be found in your project repo folder.

Copy the venv folder and contents of the resources folder into this new **Site** folder.

This **Site** folder now contains the resources for a static website deployment.  Copy the contents to a destination server and execute the startExplainerNotes.bat for the target browser to host the notes locally, e.g., ... the observatory telescope computer.

## Versioning

For the sake of tracking version history, the version numbering will follow a year, month, date numbering sequence, following by a sequence id to account for multiple versions within a single date, in the following format:

```txt
yyyy.MM.dd.#
e.g.,...  2017.05.02.0
```

Use this versioning strategy when applying label to the source.

## Contributing

Please follow these simple rules when contributing additional content or changes to the notes:

1. Add a note referencing the source of the material that is being added or changed.

1. Please follow the same formatting, and yes, although a bit tedious, cookie crumb heading and footing references.

## Authors

**Chris Ketron** - Initial compilation of LAPO source material and additional research and validation into these Markdown notes pages.
**James Classen** - Current distances JavaScript/Python contribution, additional data for notes, and code maintenance.

## Acknowledgments

Thanks to former staff of the Lake Afton Public Observatory while under the pervue of
the Wichita State University Physics Dept, for the original explainer and program notes source
material used for the creation of these Presenter Notes.

Thank you to the *ALL-Volunteer* staff of the Lake Afton Public Observatory, for the contributions and suggestions in improving these notes.
