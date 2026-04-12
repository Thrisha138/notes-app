from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
notes = []
note_id = 0

# ---------------- v1: Add Note ----------------
@app.route('/', methods=['GET', 'POST'])
def index():
    global note_id
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        notes.append({
            'id': note_id,
            'title': title,
            'desc': desc
        })
        note_id += 1
        return redirect(url_for('index'))

    return render_template('index.html', notes=notes)

# ---------------- v2: Edit Note ----------------
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    note = next((n for n in notes if n['id'] == id), None)

    if request.method == 'POST':
        note['title'] = request.form['title']
        note['desc'] = request.form['desc']
        return redirect(url_for('index'))

    return render_template('edit.html', note=note)

# ---------------- v3: Delete Note ----------------
@app.route('/delete/<int:id>')
def delete(id):
    global notes
    notes = [n for n in notes if n['id'] != id]
    return redirect('/')

# ---------------- Run App ----------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    