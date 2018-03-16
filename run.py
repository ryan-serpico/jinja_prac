from flask import Flask, render_template
app = Flask(__name__)

foo="If this shows up, then **globals() actually works."

@app.route("/")
def template_test():
	return render_template("template.html", my_string="Wheeeee!", my_list=[0,1,2,3,4,5], **globals())

if __name__ == "__main__":
	app.run(debug=True)