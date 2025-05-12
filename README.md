# Google Calendar Integration Project

This project provides integration with Google Calendar API to manage and interact with calendar events programmatically.

## Prerequisites

- Python 3.8 or higher
- Google Cloud Platform account
- Google Calendar API enabled
- OAuth 2.0 credentials configured

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Avik-creator/googlecalendarMCP
   cd googlecalendarMCP
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Google Cloud Platform Setup**
   
   a. Go to the [Google Cloud Console](https://console.cloud.google.com/)
   b. Create a new project or select an existing one
   c. Enable the Google Calendar API
   d. Create OAuth 2.0 credentials:
      - Go to APIs & Services > Credentials
      - Click "Create Credentials" > "OAuth client ID"
      - Choose "Desktop Application"
      - Download the credentials JSON file
      - Rename it to `credentials.json` and place it in the project root

5. **Environment Variables**
   
   Create a `.env` file in the project root with the following variables:
   ```
   GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
   CALENDAR_ID=your_calendar_id@group.calendar.google.com
   ```

## Usage

1. **First-time Authentication**
   ```bash
   python auth.py
   ```
   This will open a browser window for OAuth authentication. Follow the prompts to authorize the application.

2. **Running the Application**
   ```bash
   python main.py
   ```

## Features

- Create, read, update, and delete calendar events
- Set up recurring events
- Manage event attendees
- Handle event notifications and reminders

## Project Structure

```
googlecalendarMCP/
├── auth.py              # Authentication handling
├── main.py             # Main application entry point
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
├── credentials.json   # Google OAuth credentials
└── token.json        # Generated OAuth token
```

## Dependencies

The project uses the following main dependencies:
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client
- python-dotenv

## Deployed Configuration:

```json
{
  "mcpServers": {
    "google_calendar_mcp": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp-google-calendar.avikm744.workers.dev/sse"
      ]
    }
  }
}
```

## Security Notes

- Never commit your `credentials.json`, `token.json`, or `.env` file to version control
- Keep your OAuth credentials secure
- Regularly rotate your credentials and tokens

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
