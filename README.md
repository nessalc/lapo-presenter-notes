# Lake Afton Public Observatory Presenter Notes
This project uses [MKDocs](http://www.mkdocs.org/) to create a web pages providing notes of the objects and programs used at the telescope during the public programs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [Build and Deployment](#build-and-deployment) for notes on how to deploy the project on a live system.

## Prerequisites

The Presenter Notes use the following Python packages:

    mkdocs
    mkdocs-bootswatch

## Project Setup
The following are the steps I used to create the fresh Presenter Notes project, 
and these notes can be used for creating a fresh, brand-new MkDocs project.
However, if you are just cloning the existing Presenter Notes project from GitHub, 
then you can skip these steps and go directly to [Clone this Project](#clone-this-project)
    
### Install Python - the Presenter Notes are using version 3.6.1
	https://www.python.org/downloads/
	
### Virtual Environment
Create a virtual environment for the Presenter Notes Project.  Begin by creating a directory for the Python virtual environment;
I am using d:\Projects\lapoPresenterNotes\ for the virtual environments:
	
	md d:\Projects\lapoPresenterNotes
	cd d:\Projects\lapoPresenterNotes
	py -m venv env

#### Activate the virtual environment:

	env\Scripts\activate.bat
		
### Install Python Packages
    
[MKDocs](http://www.mkdocs.org/)
... from the d:\Projects\lapoPresenterNotes folder, PIP install MKDocs:

	pip install mkdocs

Theme -- [Cyborg](http://mkdocs.github.io/mkdocs-bootswatch/#cyborg) is a part of the mkdocs-bootswatch package:

	pip install mkdocs-bootswatch

### Create new MkDocs document project
From the d:\Projects\lapoPresenterNotes folder:

	mkdocs new presenterNotes
	cd presenterNotes
	
### Start MkDocs Server
To start the MKDocs dev server for testing.
From the presenterNotes folder, execute the following command

	mkdocs serve

You can then open the site for testing:
	http://127.0.0.1:8000/
	
## Clone this Project

TO DO:  ... to be completed ... !!!

## Build and Deployment
Once all editing has been completed, do a final build of the document site for deployment

	mkdocs build

TO DO:  ... to be completed ... !!!
	
## Remaining Tasks:
1. Readthedocs.org provides free hosting for MkDocs - need to set up a site and configured to auto-build upon any code changes in the linked GitHub project.
    So as changes are made to the lapoPresenterNotes, they automatically build and deploy to the readthedocs.org site.
		
2. Also, could add a CNAME to the lakeafton.org domain host to point to the readthedocs.org site… suggest docs.lakeafton.org or notes.lakeafton.org

## Versioning
For the sake of tracking version history, the version numbering will follow a year, month, date numbering sequence, following by a sequence id to account for multiple versions within a single date, in the following format:

	yyyy.MM.dd.#
	e.g.,...  2017.05.02.0

## Contributing
Please follow these simple rules when contributing additional content or changes to the notes:

1. Add a note referencing the source of the material that is being added or changed.

## Authors
Chris Ketron - initial compilation of LAPO source material and additional research and validation

## Acknowledgments
Thanks to former staff of the Lake Afton Public Observatory while under the pervue of
the Wichita State University Physics Dept, for the original explainer and program notes source
material used for the creation of these Presenter Notes.


