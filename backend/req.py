import requests

url = "http://localhost:5001/predict"
data = {
    "judul": "Kronologis Polisi Berondong Sedan Terobos Razia di Lubuklinggau",
    "narasi" : "Innalillah… Hanya Karena Lalai Terobos Razia, Mobil Berisi Satu Keluarga Ditembaki Polisi, Satu Oran..."

}

response = requests.post(url, json=data)
print(response.json())