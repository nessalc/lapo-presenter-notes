
## How to Edit and Maintain these documents

- See the GIT Hub Project Readme.md<br>
<https://github.com/caketron/lake-afton-presenter-notes>

## About these notes...
In an effort to make Observatory Presenter notes more accessible, I have taken the notes left behind by WSU staff and I am using MkDocs (Markdown) to create web-based versions.  The project is in GitHub and I have set up hooks to trigger build/deploy using ReadtheDocs.org ... check out the progress here:  <http://lake-afton-presenter-notes.readthedocs.io/en/latest>.  

I have a theme I am testing locally that converts the pages into nightvision (red text on black) so that  we can serve them up directly in the observing room at LAPO ... also, if you have any content suggestions or feedback I would really appreciate it!! ( Please create an [Issue](https://github.com/caketron/lake-afton-presenter-notes/issues) on the GitHub project: [https://github.com/caketron/lake-afton-presenter-notes/issues](https://github.com/caketron/lake-afton-presenter-notes/issues)


## Additional Things **<< To Do >>** ...

Review the [Issue](https://github.com/caketron/lake-afton-presenter-notes/issues) board on the GitHub project: [https://github.com/caketron/lake-afton-presenter-notes/issues](https://github.com/caketron/lake-afton-presenter-notes/issues) for currently identified additional work to be done.


## What's Up?

A special page has been added to these notes to support displaying images of the object that is currently in the 16" Telescope on the three monitors in the Observatory.  Just click the "what's up?" link in the upper-right corner of any notes page that has that link and the What's Up page will automatically open and display the image for that object.

If needed, you can display an empty page using the following URL:

> [http://127.0.0.1:8000/img/whats-up.html](http://127.0.0.1:8000/img/whats-up.html)

Or, you can force a title of the object into the page by providing the name parameter...
> [http://127.0.0.1:8000/img/whats-up.html?**name=Saturn**](http://127.0.0.1:8000/img/whats-up.html?name=Saturn)

Most pages will generate the full name, description and image similar to the following for object M13:

> [http://127.0.0.1:8000/img/whats-up.html?name=M13&desc=Globular%20Star%20Cluster%20in%20Hercules&image=m13-photo.jpg](http://127.0.0.1:8000/img/whats-up.html?name=M13&desc=Globular%20Star%20Cluster%20in%20Hercules&image=m13-photo.jpg)


