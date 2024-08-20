#/bin/bash

cd /home/coder/work


# Create a tokens.secrets file
FILE="/home/coder/work/protocols/test-tokens.secrets"

# Write the content to the file
cat <<EOL > "$FILE"
[discord]

webhook=https://discord.com/api/webhooks/some_webhook_url_here
channel_id=1234567890_your_channel_id_number_here

[matrix]

webhook=https://webhook.site/5e2673f1-175c-45fc-a195-f0505e97d0b6
EOL

echo "File $FILE created successfully."



# Run the notebook
/opt/conda/bin/papermill /home/coder/work/test/test.ipynb /home/coder/work/papermill/output/test-output.ipynb