
## How to Edit and Maintain these documents

- See the GIT Hub Project Readme.md<br>
<https://github.com/caketron/lake-afton-presenter-notes>

## About these notes...
In an effort to make Observatory Presenter notes more accessible, I have taken the notes left behind by WSU staff and I am using MkDocs (Markdown) to create web-based versions.  The project is in GitHub and I have set up hooks to trigger build/deploy using ReadtheDocs.org ... check out the progress here:  <http://lake-afton-presenter-notes.readthedocs.io/en/latest>.  

I have a theme I am testing locally that converts the pages into nightvision (red text on black) so that  we can serve them up directly in the observing room at LAPO ... also, if you have any content suggestions or feedback I would really appreciate it!! (either email me at [caketron@cox.net](mailto:caketron@cox.net), or create an [Issue](https://github.com/caketron/lake-afton-presenter-notes/issues) on the GitHub project: [https://github.com/caketron/lake-afton-presenter-notes/issues](https://github.com/caketron/lake-afton-presenter-notes/issues)


## Additional Things **<< To Do >>** ...

Further work to be done ...

- Add to these notes the information that Chad had done, the additional research on some of the objects we viewed in Fall 2016. It is in the LAPO Google Drive "Presenter Notes" folder.

- I have also grabbed the current "Fun Facts about..." notes from the telescope computer... and planning to work on incorporating that info into the Presenter Notes.  

- Get the vertical scroll working on the Left Nav Menu when using different themes (Cyborg theme for example...)
    
    -- [this was] fixed, and, if needed.. just need to activate following CSS property... or something similar... couldn't get this working last I tried.
    
    ``` css
    .bs-sidenav.well {
       overflow-x: auto;
    ```

- Implement a Javascript to enable/disable night vision mode by renaming the css/dayvision.css to nightvision.css...
this will work because the program only looks for the nightvision.css
and if it cannot find it... it defaults to the normal dayvision them.
If it does find the nightvision.css... then it enable the red on black for
the observing room.

    See <https://www.thesitewizard.com/javascripts/change-style-sheets.shtml> for example.

- Moon
    - hyperlink all object references between pages for quick navigation... e.g., "...in the crater [Fracastorius](#fracastorius)"

    - Alphabetize the moon objects and update the "by Phase" table with objects appropriate for the phase and cross-link all object references to the object entry

- Would like to get the fonts to match those of the LakeAfton.com site

- Customize the theme and document all necessary changes.

- Confirm that all links are active -- and review information they reference is accurate

- At initial deployment, should add a CNAME to the lakeafton.com domain host to point at
    the readthedocs.org site that is assigned for hosting the docs... e.g., 

    If you want the documentation on a subdomain point a CNAME record in your DNS to the subdomain for your project.

    For example, to make the documentation available on docs.lakeafton.com, create a CNAME record pointing to <br><http://lake-afton-presenter-notes.readthedocs.io/>.

    CNAME docs is an alias of lakeafton-doc.readthedocs.org
