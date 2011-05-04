#coding: utf-8

class Reader(object):
    def __init__(self, infile):
        self.infile = infile

    def get_meta_data(self):
        pass

class Writer(object):
    pass

class EpubReader(Reader):
    """Epub Reader
    """
    NAMESPACE = {
        'n':'urn:oasis:names:tc:opendocument:xmlns:container',
        'pkg':'http://www.idpf.org/2007/opf',
        'dc':'http://purl.org/dc/elements/1.1/'
    }
    def __init__(self, infile):
        super(EpubReader, self).__init__(infile)
        self.epub = {}

    def get_opf(self):
        """opf means Open Packaging Format
        """
        self.epub = {}
        import zipfile
        from lxml import etree

        epub = zipfile.ZipFile(self.infile)
        # find the contents metafile
        txt = zip.read('META-INF/container.xml')
        tree = etree.fromstring(txt)
        cfname = tree.xpath('n:rootfiles/n:rootfile/@full-path',namespaces=NAMESPACE)[0]
        self.epub.update({"opf" : cfname})

    def get_toc(self):
        pass

    def get_meta_data(self):
        # repackage the data
        res = {}
        for s in ['title','language','creator','date','identifier']:
            res[s] = p.xpath('dc:%s/text()'%(s),namespaces=NAMESPACE)[0]
        
