
# What's Up?

A special page has been added to these notes to support displaying images of the object that is currently in the 16" Telescope on the three monitors in the Observatory.  Just click the "what's up?" link in the upper-right corner of any notes page that has that link and the What's Up page will automatically open and display the image for that object.

NOTES:

- The **What's Up** links are only available and intended for use from within the observatory. <br/>Links will _**not**_ be available outside of the observatory network.

- _Press F11 to make the browser full-screen and hide the menu bar for the display monitors_

If needed, you can display an empty page using the following URL:

> [/img/whats-up.html](/img/whats-up.html)

You can force a title of the object into the page by providing the _name_ parameter... with centered text...

> [/img/whats-up.html?**name=Saturn**](/img/whats-up.html?name=Saturn)

... or, specify "other" for the _image_ parameter to clear an area to display an image from SkyTools:

> [/img/whats-up.html?**name=Saturn&image=other**](/img/whats-up.html?name=Saturn&image=other)

Most pages will generate the full _name_, _description_ and _image_ parameters similar to the following,  for object M13:

> [/img/whats-up.html?name=M13&desc=Globular%20Star%20Cluster%20in%20Hercules&image=m13.jpg](/img/whats-up.html?name=M13&desc=Globular%20Star%20Cluster%20in%20Hercules&image=m13.jpg)

---

# Custom What's Up Form

Use the following to display a customized What's Up page:

<form action="/img/whats-up.html" target="_blank">
Object Name<br/>&nbsp;&nbsp;&nbsp;<input type="text" name="name"><br/>
Object Description<br/>&nbsp;&nbsp;&nbsp;<textarea cols="100" name="desc"></textarea><br/>
&nbsp;&nbsp;&nbsp; - use of HTML codes, like line break: &lt;br/&gt;, are allowed<br/>
Object Image Filename<br/>&nbsp;&nbsp;&nbsp;<input type="text" name="image"><br/>
&nbsp;&nbsp;&nbsp; - use "other" for the image name to display a blank image area and to place the logo and description areas to the left<br/>
&nbsp;&nbsp;&nbsp; - referenced image files must be located in the_**site\img\whats-up**_ folder
<br/><br/>
&nbsp;&nbsp;&nbsp;<input type="submit" value="What's Up?">
</form>
