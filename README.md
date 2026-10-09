# LiteBot
* A chatbot that uses Retrieval-Augmented Generation to answer questions about me!

## Highlights:
* Real-time messaging
* Error handling on both the server and client side

## Target Environment:
* A proprietary cloud built on top of AWS, partially composed of standard server CPUs (x86_64), that is provided by Render

### How To Run
* Clone the repo
```
git clone https://github.com/lucasthormann/lite-bot.git
```

#### Backend
* Navigate to backend & create virtual environment
```
cd backend && python3 -m venv venv
```
* Activate the venv & install requirements using pip
```
source venv/bin/activate
pip install -r requirements.txt
```
* Run the backend
```
python3 app.py
```

#### Frontend
* Navigate to frontend
```
cd frontned
```
* Install dependencies using npm
```
npm install
```
* Run the frontend
```
npm run dev
```

### How To Use
* Open up a browser and access the app via this URL
```
http://localhost:5173/
```
