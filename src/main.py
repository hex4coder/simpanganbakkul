Xi = [26,345,63,102]
Fi = [34,33,100,23]

sigmaFi = 0
sigmaFiXi = 0

def XiKaliFi():
    n = len(Xi)
    XiFi =[]
    for i in range(0, n):
        hasilKali = Xi[i] * Fi[i]
        XiFi.append(hasilKali)
    return XiFi

print("Data Xi")
print(Xi)
print("")

print("Data Fi")
print(Fi)
print("")

print("Hasil kali Xi.Fi")
print(XiKaliFi())
print("")

for fi in Fi:
    sigmaFi += fi

for fixi in XiKaliFi():
    sigmaFiXi += fixi

print("Sigma Fi")
print(sigmaFi)
print("")

XBar = sigmaFiXi / sigmaFi

print("Sigma Xi.Fi")
print("XBar")
print(XBar)
print("")

XiminXBar = []

for xi in Xi:
    XiminXBar.append(round(abs(xi - XBar), 1))

print("|Xi-XBar|")
print(XiminXBar)
print("")

FidotXiminXbar = []
sigmaFidotXiminXbar = 0
n = len(XiminXBar)
for i in range(0, n):
    hasilKali = Fi[i] * XiminXBar[i]
    sigmaFidotXiminXbar += hasilKali
    FidotXiminXbar.append(hasilKali)

simpanganRata2 = sigmaFidotXiminXbar / sigmaFi

print("Fi.|Xi-XBar|")
print(FidotXiminXbar)
print("")


print("Simpangan Rata-rata")
print(simpanganRata2)
print("")
    