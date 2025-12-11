class Kitap():
    def __init__(self,name,author,year):
        self.name=name
        self.author=author
        self.year=year
    
    def __str__(self):
        return f"\033[34mKitap Adı:\033[0m {self.name}   \033[34mYazar:\033[0m {self.author}   \033[34mYıl:\033[0m {self.year}"

class Kütüphane():
    def __init__(self):
        self.books=[]

    def add_book(self,q):
        self.books.append(q)     #q yeni eklenecek olan Kitap nesnesini temsil eder, self parametresi eklenecek kitabı library nesnesine götürür
    
    def remove_book(self,q1):
        self.books.remove(q1)

    def search_by_name(self,name_search):
        if name_search.lower() not in [i.name for i in self.books]:print(f"\033[34m{name_search.title()} Adlı Kitap Bulunamadı.\033[0m")
        for book in self.books:
            if book.name.lower()==name_search.lower():
                print("\n\033[34mArama Sonuçları:\033[0m")
                print(book)
                break
    
    def search_by_author(self,author_search):
        if author_search.lower() not in [i.author.lower() for i in library.books]:
            print(f"\033[34m{author_search.title()}\033[0m Adlı Yazarın Hiçbir Kitabı Bulunamamıştır.")
        else:
            print("\n\033[34mArama Sonuçları:\033[0m")
            for book in self.books:
                if book.author.lower()==author_search.lower():
                    print(book)
    
    def list_all(self):
        if len(self.books)!=0:
            print("\033[34m\033[4mTüm Kitaplar \033[0m")
            [print(book) for book in self.books]
        else:print("\033[34mKütüphanede Listelenecek Kitap Bulunmamaktadır.\033[0m")
        

library=Kütüphane()

print("Kütüphane Kitap Arama Sistemi")
while True:
    try:
        choice=int(input("\n\n1. Kitap Ekle\n2. Kitap Sil\n3. Kitap Ara (İsme Göre)\n4. Kitap Ara (Yazara Göre)\n5. Tüm Kitapları Listele\n6. Çıkış\n>>\033[33mİşlem Seçiniz (1-6)\033[0m"))
        if choice>6 or choice<1:
            raise ValueError
    except:
        print("\033[33mGeçerli Bir İşlem Seçiniz\033[0m")
        continue
    if choice==1:
        a=input("Kitap Adı:")
        b=input("Yazar:")
        try:
            c=int(input("Yayın Yılı:"))
        except:
            print("\033[33mGeçerli Bir Yayın Yılı Giriniz\033[0m")
            continue
        library.add_book(Kitap(a,b,c))
        print("\033[32m{}\033[0m Başarıyla Kütüphaneye \033[42mEklendi\033[0m".format(a.title()))

    elif choice==2:
        d=input("Kitap Adı (SİLİNECEK!!):")
        if d.lower() in [i.name.lower() for i in library.books]:
            for i in library.books:
                if d.lower()==i.name.lower():    
                    print("\033[31m{}\033[0m Kütüphaneden Başarıyla \033[41mSilindi!\033[0m".format(d.title()))
                    library.remove_book(i)
        else:print(f"\033[34m{d.title()} Adlı Kitap Bulunamadı.")

    elif choice==3:
        searchN=input("Aradığınız Kitabın Adını Girin:")
        library.search_by_name(searchN)

    elif choice==4:
        searchA=input("Aradığınız Yazarın Adını Girin:")
        library.search_by_author(searchA)

    elif choice==5:
        library.list_all()

    elif choice==6:
        print("\033[31m \033[1mÇıkış Yapılıyor...\033[0m\n")
        exit()