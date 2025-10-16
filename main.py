from fastapi import FastAPI
import uvicorn

app = FastAPI()


#Get Journal Entries
@app.get("/journal")
def read_root():
    return {"message": "Hello, World!"}
#Add Journal Entry
@app.post("/journal")
def read_root():
    return {"message": "Hello, World!"}

#Get Advice
@app.get("/advice")
def read_root():
    return {"message": "Hello, World!"}

#Add Advice
@app.post("/advice")
def read_root():
    return {"message": "Hello, World!"}

#Get Mood Analysis with sentimental analysis From Journal Entries
@app.get("/mood-analysis")
def read_root():
    return {"message": "Hello, World!"}

# Get Stress Analysis from journal entries
@app.get("/stress-analysis")
def read_root():
    return {"message": "Hello, World!"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)