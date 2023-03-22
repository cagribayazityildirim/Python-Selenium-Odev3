'''
HTML NEDİR ?
HTML (HyperText Markup Language), web sayfalarının yapısını tanımlayan bir işaretleme dilidir.
Web sayfaları, HTML etiketleri yardımıyla yapılandırılır ve bu etiketler sayfa içeriğinin anlamını belirler.
Web Arayüz Programlama’nın ilk ayağı olarak adlandırılabilecek HTML için Web’in iskeleti diyebiliriz.
Bütün web sayfalarında kullanılan bir standarttır. HTML bir programlama dili değildir.
Adında da belirtildiği şekilde işaretleme (markup) dilidir. Sunulmak istenen veri etiketler yardımıyla işaretlenir.
HTML için çeşitli etiketler vardır. Etiketler yardımıyla HTML içeriği anlamlandırılır. Örneğin başlık yapılmak istenen metin, başlık etiketiyle işaretlenir. 
Sadece HTML ile web sayfaları hazırlamak mümkündür. Bu web sayfaları Statik Web Sayfaları olarak adlandırılır.

En Çok Kullanılan HTML Etiketleri
Etiket Adı	Açıklaması
<!-- .. -->	HTML yorum satırı
<!DOCTYPE html>	Belgenin türünü belirlemek için kullanılır. Belgenin en üstünde bulunması gerekir.
<html>	HTML belgesinin kapsayıcı kök elemanını tanımlar.
<head>	Sayfanın meta verilerini ve diğer ek bilgilerini içerir. <html> etiketinden sonra yazılır.
<meta>	Bir HTML belgesi hakkında meta verileri tanımlar. Genllikle <head>alanı içerisinde yazılır
<link>	Bir HTML belgesine bir harici kaynak bağlamak için kullanılır. Genellikle bir stil belgesi eklemek için kullanılır ve <head>alanı içerisinde yazılır
<body>	Belgenin gövdesini oluşturmak için <head> </head> alanından sonra kullanılır.
<a>	Köprü metin linkini tanımlar.
<abbr>	Kısaltma Tanımlar title="Uzun İsmi" şeklinde öznitelik eklenir.
<address>	Sayfanın sahibi için iletişim bilgilerini belirtir.
<article>	Makalenin içeriğini ya da sayfanın içeriğini belirtmek için kapsayıcı olarak kullanılır.
<aside>	Sayfanın içeriği dışındaki diğer yan taraf içeriklerini belirlemek için kullanılır.
<audio>	Gömülü Ses dosyasını belirtmek için.
<b>	Bold/kalın metin belirtmek için.
<blockquote>	Başka bir kaynaktan ya da bir kişiden alıntı yapmak ve atıfta bulunmak için kullanılır.
<div>	Sayfadaki bölümleri ve kutucukları belirlemek için kullanılır.
<h1..h6>	Başlık ve alt başlık etiketlerini tanımlar
<p>	HTML sayfasındaki paragrafları tanımlar.
<em>	Vurgulanmış metni belirtmek için kullanılır.
<strong>	önemli metni ya da hedef anahtar kelimeyi tanımlar.
<code>	kod metin gösterimini belirtmek için kullanılır
<header>	Sayfanın üst içeriğini ya da üst barı göstermek için kullanılır
<footer>	Sayfanın alt içeriğini ya da alt barı göstermek için kullanılır
<section>	HTML sayfasındaki ayrı bir bölümü belirtmek için kullanılır.
<main>	Sayfadaki ana içeriği belirtmek için kullanılır.
<figure>	Müstakil, bağımsız içeriği belirtmek için kullanılır
<figacaption>	<figure< öğesine başlık metni için kullanılır.
<hr>	İçerikte bir ayıraç ve tematik değişikliği belirtmek için kullanılır.
<br>	içeriğin ve metnin bir alt satırdan devam etmesi için kullanılır.
<i>	Metnin istenen bölümünü düz yazıdan ayırır ve italik olarak belirtir. İcon-font eklenmesinde de bu etiket kullanılabilir.
<img>	Resim içeriğini ve dosyasını tanımlar src="" ile resim yolu çağırılır, alt="Resim Başlığı" özniteliği ile de resim adı yazılır.
<form>	Kullanıcı için bir giriş formu tanımlar.
<input>	Form üzerinde bir giriş kontrolü tanımlar.
<label>	<input> elemanı için bir etiket tanımlar.
<select>	Form içerisinde açılır liste elemanlarını tanımlar.
<optgroup>	Açılır listede ilgili içeriğin bir grubunu tanımlar
<option>	Açılır listede bir seçenek tanımlamak için kullanılır.
<textarea>	Multi-line/çok satırlı kullanıcı giriş bilgisi tanımlamak için kullanılır.
<button>	Tıklanabilir bir buton tanımlamak için kullanılır.
<table>	Sayfaya tablo eklemek için kullanılır.
<thead>	Tablonun üst içeriğini eklemek için kullanılır.
<tbody>	Tablonun gövde grup içeriklerini eklemek için kullanılır.
<tr>	<table> içerisindeki bir satırı belirtmek için kullanılır.
<td>	Tablo satırındaki her bir hücreyi belirlemek için kullanılır.
<tfoot>	Tablonun alt kısmını eklemek için kullanılabilir.
<ul>	Numaralandırılmamış/sıralanmamış bir liste oluşturmak için kullanılır.
<ol>	Sıralı bir liste tanımlar.
<li>	<ul>, <ol> liste elemanları içerisinde bir liste öğesini tanımlamak için kullanılır.

HTML Locators ?
Tarayıcıyı açtık ve bir siteye girdik şimdi bu sitede neler yapabiliriz düşünelim.
Belirli bir alana tıklayabilir, inputların veya text elemanlarının içerisini doldurabiliriz.  Locators(Konumlandırıcı), Selenium IDE’ye hangi web tabanlı objeler üzerinde çalışması gerektiğini söyleyen bir komuttur. 
Doğru elementin tanımlanması, otomasyon oluşturmanın ön koşuludur. Site üzerindeki bir elemente örneğin giriş butonuna selenium ile tıklama işlemi yaptırmak istediğimizde bu işlemi locator’lar aracılığıyla yaparız.
Selenium ile geliştirmek istediğimiz test otomasyonlarında locator’ları kullanarak ilgili alanlara veri gönderebilir, tıklama işlemi yaptırabilir, var olan içeriği temizleyebiliriz. Bunlar ‘By’ objesi olarak oluşturulur. En yaygın locator çeşitleri;

1)ID
2)Name
3)ClassName
4)TagName
5)LinkText
6)CssSelector
7)XPath
Web sitelerinde tagname’ler bulunur. Bu tagname’lerin sahip olduğu stil, name, id gibi attribute’ler vardır. 
Selenium’un anlayacağı şekilde nesneleri web elementlere çevirirken ilk önce id’si ve name’i var mı diye bakılır yok ise CssSelector ve Xpath ile nesneyi bulmaya çalışırız.

ID: HTML öğelerine eşsiz bir tanımlayıcı veren "id" özelliği, öğeleri belirlemenin en kolay yolu olarak kabul edilir.
Name: HTML öğelerine isim vermek için "name" özelliği kullanılır. Bu özellik, özellikle form öğeleri için yararlıdır.
Class: "class" özelliği, HTML öğelerine bir veya daha fazla sınıf adı atamanızı sağlar.
Tag Name: HTML öğelerine "tag name" ile referans verilebilir.
Link Text: Bu yöntem, bir bağlantıyı metin içeriğiyle belirler.
Partial Link Text: Bu yöntem, bağlantı metninin bir kısmını kullanarak bağlantıyı belirler.
CSS Selector: CSS seçicileri, HTML öğelerinin belirli özelliklerine göre seçilmesini sağlar.
XPath: XPath, XML tabanlı belgelerdeki öğeleri belirlemek için kullanılan bir dil ve HTML sayfalarında da kullanılabilir.

Selenium'da Aksiyonlar ?

1. get(url): Belirtilen URL'ye gitmek için kullanılır.
2. find_element(): Belirtilen özelliklere göre bir elementi (bir metin kutusu, bir buton, bir bağlantı vb.) bulmak için kullanılır.
3. send_keys(keys) : Bir elemente metin girmek için kullanılır.
4. click() : Bir elementi tıklamak için kullanılır.
5. clear() : Bir metin kutusundaki mevcut metni silmek için kullanılır.
6. submit() : Bir formu göndermek için kullanılır.
7. back() : Önceki sayfaya dönmek için kullanılır.
8. forward() : İleri sayfaya gitmek için kullanılır.
9. refresh() : Sayfayı yenilemek için kullanılır.





'''