# ace

Google Cloud Associate Cloud Engineer practice quiz and study notes.

## Quiz

The static site is in `docs/`. To preview it locally, run:

```bash
python3 -m http.server 8000 -d docs
```

Then open <http://localhost:8000>.

## Update questions

Question explanations live in `questions/`. After adding or changing a question, regenerate the quiz data:

```bash
python3 build_quiz.py
```

Commit both the question file and the updated `docs/questions.js`.

## GitHub Pages

In this repository's **Settings → Pages**, choose **Deploy from a branch**, then select **main** and **/docs** and save. The site will be at <https://lamji.github.io/ace/> after the Pages deployment finishes.
