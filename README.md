# Minimalistic telegram bot to mention every chat member
Sometimes one really wants to make a group poll or draw attention to a certain message in a given chat,
but telegram does not have a built-in support for that.  

## Mention everyone
That is what this small project is supposed to fix by providing
`@all`, `@everyone` and optionally `@<BOT_USERNAME>` to mention (`@<USERNAME>`)every group member.

## Turn off mentioning
Want to opt out? Then `/toggle_tag` is for you. Bot will stop mentioning you in this group until you use the command again
## Running locally
Create a virtual environment (optional)
```bash
python3 -m venv .venv && source .venv/bin/activate
```
Create a `.env` file and fill it according to `.env-template`\
Then install the dependencies and launch the bot itself
```bash
pip install -r requirements.txt && python3 -m src.main
```
## Running using Docker
Make sure that `tag-all.db` exists before running the following command.\
Otherwise, Docker will create a folder named `tag-all.db`
```bash
docker build -t tag-all-bot https://github.com/om3lette/tag-all-bot.git &&\
docker run \
-v <YOUR_APPLICABLE_PATH>/tag-all.db:/tag-all-bot/tag_all.db \
-v <YOUR_PATH>/.env:/tag-all-bot/.env \
-d --name tag-all-bot --rm tag-all-bot
```