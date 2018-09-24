# Lake Afton Public Observatory Presenter Notes
This project uses [MKDocs](http://www.mkdocs.org/) to create web pages providing notes of the objects and programs used at the telescope during the public programs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [Build and Deployment](#build-and-deployment) below for notes on how to deploy the project on a live system.

## Build Environment
This project was built using the following environment components:

[Visual Studio Code](https://code.visualstudio.com/)

[Git for Windows](https://git-scm.com/download/win)

[Python 3.6.1](https://www.python.org/downloads/)

## Project Setup
The following are the steps I used to create the fresh Presenter Notes project, 
and these notes can be used for creating a fresh, brand-new MkDocs project.
However, if you are just cloning the existing Presenter Notes project from GitHub, then you can skip these steps and go directly to [Clone this Project](#clone-this-project)
 	
### Virtual Environment
Create a virtual environment for the Presenter Notes Project.  
Begin by creating a directory for the Python virtual environment;

Example...
```
md c:\virtz
md c:\virtz\lake-afton-presenter-notes
virtualenv c:\virtz\lake-afton-presenter-notes
```

#### Activate the virtual environment:

You can do this from any folder location, recommend from your local github\lake-afton-presenter-notes project folder
```
c:\virtz\lake-afton-presenter-notes\Scripts\activate.bat
```

## Prerequisites

See the pip-dependencies.txt file for the Python package requirements for the LAPO Presenter Notes:

### Install Python Packages

**Short-cut**: to install *ALL* pip dependencies:
The following *must* be done from your local github\lake-afton-presenter-notes project folder, where the pip-dependencies.txt exists...

```python
pip install -r pip-dependencies.txt
```

... for manual installation ... do the following...

From the d:\gitLAPO\lake-afton-presenter-notes\ folder, PIP install MKDocs:

```python
pip install mkdocs
```
reference [MKDocs](http://www.mkdocs.org/) for more information 

Theme 
This project uses the MkDocs Bootswatch Theme: [Cyborg](http://mkdocs.github.io/mkdocs-bootswatch/#cyborg)

```python
pip install mkdocs-bootswatch
```

### Start MkDocs Server
To start the MKDocs dev server for testing.
From the presenterNotes folder, execute the following command

	mkdocs serve

You can then open the local site for testing:<br/>
	http://127.0.0.1:8000/
	
## Clone this Project

From the GitHub repository: https://github.com/caketron/lake-afton-presenter-notes
select Clone and copy the URL to the repo: https://github.com/caketron/lake-afton-presenter-notes.git

Then from your local project folder (I am using c:\git\github), execute the following git command:
```git
git clone https://github.com/caketron/lake-afton-presenter-notes
```

## Build and Deployment
Once all editing has been completed, do a final build of the document site for deployment

```
mkdocs build
```

<< TO DO >>:  ... to be completed ... !!!
	
## Versioning
For the sake of tracking version history, the version numbering will follow a year, month, date numbering sequence, following by a sequence id to account for multiple versions within a single date, in the following format:

	yyyy.MM.dd.#
	e.g.,...  2017.05.02.0

Use this versioning strategy when applying label to the source.

## Contributing
Please follow these simple rules when contributing additional content or changes to the notes:

1. Add a note referencing the source of the material that is being added or changed.

1. Please follow the same formatting, and yes, although a bit tedious, cookie crumb heading and footing references.

## Authors
**Chris Ketron** - Initial compilation of LAPO source material and additional research and validation into these MarkDown notes pages.

## Acknowledgments
Thanks to former staff of the Lake Afton Public Observatory while under the pervue of
the Wichita State University Physics Dept, for the original explainer and program notes source
material used for the creation of these Presenter Notes.

Thank you to the *ALL-Volunteer* staff of the Lake Afton Public Observatory, for the contributions and suggestions in improving these notes.
