# Esperimenti con Bokeh

Avendo la necessità di sperimentare grafici animati via web,
ho prodotto alcuni semplici proof-of-concept con [Bokeh](http://bokeh.pydata.org)

Presa l'ispirazione da questo "collega" partecipante alla MakerFaire 2013 ;)
https://www.continuum.io/content/painless-streaming-plots-bokeh

che narrava della possibilità di grafici animati dalla 0.3 di Bokeh
ho sperimentato partendo da:

https://www.continuum.io/content/painless-streaming-plots-bokeh

e da

http://bokeh.pydata.org/en/latest/docs/user_guide/server.html

e ho realizzato questi.

La cosa interessante è che sono grafici web aggiornati via callback
javascript.

... e senza scrivere una riga di javascript!

## Come eseguire il codice

`bokeh serve --show myfake2dplot.py`

o

`bokeh serve --show myfake2dplotonlycircles.py`

o infine

`bokeh serve --show mycerchiautoaggiornantiacaso.py`

## Ringraziamenti

Si ringrazia @Azzeccagarbugli e il [MakerSpace della Biblioteca di Fabriano](http://www.bibliotecafabriano.it)
per aver "dato il la" all sperimentazione e ancora e ancora!
