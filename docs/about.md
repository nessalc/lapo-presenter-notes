
## How to Edit and Maintain these documents

- See the GIT Hub Project Readme.md<br>
<https://github.com/caketron/lake-afton-presenter-notes>

## Things To Do ...

Further work to be done ...

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

- Fix the following errors during `mkdocs serve` (see source doc for commented warnings...)
<!--WARNING -  Template variable warning: 'page_description' is being deprecated and will not be available in a future version. 
            Use 'config.site_description' instead.
WARNING -  Template variable warning: 'site_author' is being deprecated and will not be available in a future version. 
            Use 'config.site_author' instead.
WARNING -  Template variable warning: 'canonical_url' is being deprecated and will not be available in a future version. 
            Use 'page.canonical_url' instead.
WARNING -  Template variable warning: 'favicon' is being deprecated and will not be available in a future version. 
            Use '{{ base_url }}/img/favicon.ico' instead.
WARNING -  Template variable warning: 'page_title' is being deprecated and will not be available in a future version. Use 'page.title' instead.
WARNING -  Template variable warning: 'site_name' is being deprecated and will not be available in a future version. Use 'config.site_name' instead.
WARNING -  Template variable warning: 'google_analytics' is being deprecated and  will not be available in a future version. 
            Use 'config.google_analytics' instead.
WARNING -  Template variable warning: 'current_page' is being deprecated and will not be available in a future version. Use 'page' instead.
WARNING -  Template variable warning: 'copyright' is being deprecated and will not be available in a future version. Use 'config.copyright' instead.
WARNING -  Template variable warning: 'include_nav' is being deprecated and will not be available in a future version. Use 'nav|length>1' instead.
WARNING -  Template variable warning: 'include_next_prev' is being deprecated and will not be available in a future version. 
            Use '(page.next_page or page.previous_page)' instead.
WARNING -  Template variable warning: 'repo_url' is being deprecated and will not be available in a future version. Use 'config.repo_url' instead.
WARNING -  Template variable warning: 'homepage_url' is being deprecated and will not be available in a future version. Use 'nav.homepage.url' instead.
WARNING -  Template variable warning: 'previous_page' is being deprecated and will not be available in a future version. Use 'page.previous_page' instead.
WARNING -  Template variable warning: 'next_page' is being deprecated and will not be available in a future version. Use 'page.next_page' instead.
WARNING -  Template variable warning: 'repo_name' is being deprecated and will not be available in a future version. Use 'config.repo_name' instead.
WARNING -  Your theme does not appear to contain a 'main.html' template. The 'base.html' template was used instead, which is deprecated. 
            Update your theme so that the primary entry point is 'main.html'.
WARNING -  Template variable warning: 'toc' is being deprecated and will not beavailable in a future version. Use 'page.toc' instead.
WARNING -  Template variable warning: 'meta' is being deprecated and will not be available in a future version. Use 'page.meta' instead.
WARNING -  Template variable warning: 'content' is being deprecated and will not be available in a future version. Use 'page.content' instead.-->
