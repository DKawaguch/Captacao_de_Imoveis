import subprocess

def start_streamlit():
    subprocess.run(["streamlit", "run", "src/main.py"])

if __name__ == "__main__":
    start_streamlit()