# buat folder ==> C:/data/db
# cd c:/ProgramFiles/MongoDB/server/version
# mongod --dbpath c:/data/db

#aktivasi server

# buka 1 cmd lagi untuk koding. Biarkan cmd yang lama untuk koneksi ke server.
# > show dbs (untuk menampilkan list database)
# > db (di database apa kita berada)
# > use tokoonline (membuat sekaligus pindah ke database tokoonline)
# > db.createCollection('seller') (membuat table baru bernama 'seller')
# > db.createUser({user:'ridho', pwd: '12345', roles: ['dbAdmin', 'readWrite]}) (membuat roles pada satu database)
# > db.seller.insert({nama: 'Andi', usia: '22'}) (menambah satu data)
# > db.seller.insert([{nama: 'Budi', usia: 24}, {nama: 'Caca', usia: 23}]) menambah lebih dari satu data)
# > db.seller.find() / db.seller.find().pretty() (menampilkan data pada seller)
# > db.seller.insert({nama: 'Dedi', usia: 25, kota: 'Jakarta'}) (menambah data baru dengan keys baru)
# > db.seller.remove({kota: 'Jakarta'}) (menghapus data dengan value kota = 'Jakarta')

