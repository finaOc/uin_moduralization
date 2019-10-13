nama = 'Fina Urbatul Farikha'
program = 'tekanan'

print(f'program {program} oleh {nama}')

def hitung_tekanan(gaya, luas):
    tekanan = gaya / luas
    print(f'gaya = {gaya} dalam bidang seluas = {luas}')
    print(f'sehingga tekanan = {tekanan} N/m^2')
    return tekanan

# gaya = 100
# luas = 20
tekanan = hitung_tekanan(100, 20)