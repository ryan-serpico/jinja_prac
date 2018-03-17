from flask import Flask, render_template
import markdown
import io
app = Flask(__name__)

input_file = io.open("python_md_test.md", mode="r", encoding="utf-8")
text = input_file.read()
content = markdown.markdown(text)

# @app.route("/")
# def template_test():
# 	return render_template("template.html", **globals())
	# Something needs to be added to this function so that it can spit out an HTML file. Each file name needs to have a different name. We could give each one a number that has 1 added to it each time the function runs. We could also set it up so that the first <h1> tag is the HTML file name.
	# Doing the latter would allow for us to have the bot spit out the URL of the uploaded story.


@app.route("/")
def template_test():
	with open('index.html', 'wb') as f:
		return f.write(render_template('template.html', **globals()))

# Open a connection with the FTP server and pass through the file that the previous function spat out.

# The bot should also accept images. Using Markdown's syntax, editor's would add "![Alt text](/path/to/img.jpg)" in the story to add an image. So the bot should accept images, and dump it into a media folder. For example, if an editor wanted to add an image of a butterfly, it could be "![Butterfly](/media/butterfly.jpg)" within the story. So we need to write another FTP function.

# Return the story's URL, which is hypothetically possible with the idea I mentioned in the render_template function comments.


if __name__ == "__main__":
	app.run(debug=True)