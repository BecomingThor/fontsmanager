import sqlite3
import os

FONTPATH = 'C:\\Users\\brian\\Documents\\FontsManager\\fonts'

class Handler():
    def __init__(self):
        pass

    def db(self, query):
        try:
            #establish connection
            sqliteConnection = sqlite3.connect('fonts.db')
            cursor = sqliteConnection.cursor()

            #dbquery
            cursor.execute(query)
            sqliteConnection.commit()
            res = cursor.fetchall()

        #Error / exceptions handlen
        except sqlite3.Error() as e:
            print('Error: %s' %str(e))
        except sqlite3.OperationalError as e:
            print('Error: %s' %str(e))

        finally:
            #close connection
            cursor.close()
            if sqliteConnection:
                sqliteConnection.close()
            print(query)
            print('success:')
            print(res)
            return res

class Category():
    def __init__(self):
        pass

    GET_ALL_CATEGORIES = 'SELECT * FROM tcategorys;'

    #@param array
    def searchCategory(self, chosencategory):
        stringify = ' OR '.join(chosencategory)
        query = ("""SELECT tfonts.cfont, tcategorys.ccategory
		FROM category_font
		INNER JOIN tfonts ON category_font.font_id=tfonts.font_id
		INNER JOIN tcategorys ON category_font.category_id=tcategorys.category_id
		WHERE ccategory = """)
        query += stringify
        return query

    def insertCategory(self, newCategory):
        query = """INSERT OR IGNORE INTO tCategorys (ccategory) VALUES """
        for category in newCategory:
            if category == newCategory[-1]:
                newcategory = "('{}');".format(category)
            else:
                newcategory = "('{}'),".format(category)
            query += newcategory
        return query

    def org_add_Category(self, Font, Category):
        catId = Handler().db(getId().getCategoryId(Category))
        fontId = Handler().db(getId().getFontId(Font))
        query = """INSERT OR IGNORE INTO category_font (font_id, category_id) VALUES """
        if len(catId) > 1 and len(fontId) == 1:
            for id in catId:
                if id == catId[-1]:
                    orgCat_Id = "('{}','{}');".format(fontId[0][0], id[0])
                else:
                    orgCat_Id = "('{}','{}'),".format(fontId[0][0], id[0])
                query += orgCat_Id
        elif len(fontId) > 1 and len (catId) == 1:
            for font in fontId:
                if id == fontId[-1]:
                    orgCat_Id = "('{}','{}');".format(id[0], catId[0][0])
                else:
                    orgCat_Id = "('{}','{}'),".format(id[0], catId[0][0])
                query += orgCat_Id
        elif len(fontId) == 1 and len(catId) == 1:
            orgCat_Id = "('{}','{}');".format(fontId[0][0], catId[0][0])
            query += orgCat_Id
        else:
            print('error wrong typ or number')
        return(query)

    def org_rmv_Category(self, Font, Category):
        catId = Handler().db(getId().getCategoryId(Category))
        fontId = Handler().db(getId().getFontId(Font))
        query = """DELETE FROM category_font WHERE """
        if len(catId) > 1 and len(fontId) == 1:
            for id in catId:
                if id == catId[-1]:
                    orgCat_Id = "(font_id = '{}' and category_id = '{}');".format(fontId[0][0], id[0])
                else:
                    orgCat_Id = "(font_id = '{}' and category_id = '{}') OR ".format(fontId[0][0], id[0])
                query += orgCat_Id
        elif len(fontId) > 1 and len (catId) == 1:
            for font in fontId:
                if id == fontId[-1]:
                    orgCat_Id = "( font_id = '{}' and category_id = '{}');".format(id[0], catId[0][0])
                else:
                    orgCat_Id = "(font_id = '{}' and category_id = '{}') OR".format(id[0], catId[0][0])
                query += orgCat_Id
        elif len(fontId) == 1 and len(catId) == 1:
            orgCat_Id = "(font_id = '{}' and category_id = '{}');".format(fontId[0][0], catId[0][0])
            query += orgCat_Id
        else:
            print('error wrong typ or number')
        print(query)
        return(query)

class getId():
    def __init__(self):
        pass

    def getCategoryId(self, category):
        query = ("""SELECT category_id
		FROM tcategorys
		WHERE """)
        for item in category:
            if item == category[-1]:
                orgCat = "ccategory = '{}';".format(item)
            else:
                orgCat = "ccategory = '{}' OR ".format(item)
            query += orgCat
        return query

    def getFontId(self, font):
        query = ("""SELECT font_id
		FROM tfonts
		WHERE """)
        for item in font:
            if item == font[-1]:
                orgfont = "cfont = '{}';".format(item)
            else:
                orgfont = "cfont = '{}' OR ".format(item)
            query += orgfont
        return query

    def getTagId(self, tag):
        query = """SELECT tags_id FROM ttags WHERE """
        for item in tag:
            if item  == tag[-1]:
                orgTag = "ctags = '{}';".format(item)
            else:
                orgTag = "ctags = '{}' OR ".format(item)
            query += orgTag
        return query

class Tag():
    def __init__(self):
        pass

    GET_ALL_TAGS = 'SELECT * FROM tTags;'

    #@param array
    def searchTags(self, chosentags):
        stringify = ' OR '.join(chosentags)
        query = ("""SELECT tfonts.cfont, tTags.ctags
		FROM font_tag
		INNER JOIN tfonts ON font_tag.font_id=tfonts.font_id
		INNER JOIN tTags ON font_tag.tag_id=tTags.tags_id
		WHERE ctags =""")
        query += stringify
        return query

    def insertTag(self, newTags):
        query = """INSERT OR IGNORE INTO tTags (ctags) VALUES """
        for tag in newTags:
            if tag == newTags[-1]:
                newtag = "('{}');".format(tag)
            else:
                newtag = "('{}'),".format(tag)
            query += newtag
        return query

    def org_add_Tag(self, Font, Tag):
        tagId = Handler().db(getId().getTagId(Tag))
        fontId = Handler().db(getId().getFontId(Font))
        query = """INSERT OR IGNORE INTO font_tag (font_id, tag_id) VALUES """
        if len(tagId) > 1 and len(fontId) == 1:
            for id in tagId:
                if id == tagId[-1]:
                    orgTag_Id = "('{}','{}');".format(fontId[0][0], id[0])
                else:
                    orgTag_Id = "('{}','{}'),".format(fontId[0][0], id[0])
                query += orgTag_Id
        elif len(fontId) > 1 and len (tagId) == 1:
            for font in fontId:
                if id == fontId[-1]:
                    orgTag_Id = "('{}','{}');".format(id[0], tagId[0][0])
                else:
                    orgTag_Id = "('{}','{}'),".format(id[0], tagId[0][0])
                query += orgTag_Id
        elif len(fontId) == 1 and len(tagId) == 1:
            orgTag_Id = "('{}','{}');".format(fontId[0][0], tagId[0][0])
            query += orgTag_Id
        else:
            print('error wrong typ or number')
        print(query)
        return(query)

    def org_rmv_Tag(self, Font, Tag):
        tagId = Handler().db(getId().getTagId(Tag))
        fontId = Handler().db(getId().getFontId(Font))
        query = """DELETE FROM font_tag WHERE """
        if len(tagId) > 1 and len(fontId) == 1:
            for id in tagId:
                if id == tagId[-1]:
                    orgTag_Id = "(font_id = '{}' and tag_id = '{}');".format(fontId[0][0], id[0])
                else:
                    orgTag_Id = "(font_id = '{}' and tag_id = '{}') OR ".format(fontId[0][0], id[0])
                query += orgTag_Id
        elif len(fontId) > 1 and len (tagId) == 1:
            for font in fontId:
                if id == fontId[-1]:
                    orgTag_Id = "( font_id = '{}' and tag_id = '{}');".format(id[0], tagId[0][0])
                else:
                    orgTag_Id = "(font_id = '{}' and tag_id = '{}') OR".format(id[0], tagId[0][0])
                query += orgTag_Id
        elif len(fontId) == 1 and len(tagId) == 1:
            orgTag_Id = "(font_id = '{}' and tag_id = '{}');".format(fontId[0][0], tagId[0][0])
            query += orgTag_Id
        else:
            print('error wrong typ or number')
        print(query)
        return(query)

class Font():
    def __init__(self):
        pass

    GET_ALL_FONTS = 'SELECT * FROM tfonts;'

    def importFonts(self):
        arr = os.listdir(FONTPATH)
        query = """INSERT OR IGNORE INTO tfonts (cfont, favourite, filepath) VALUES """
        for font in arr:
            directFONTPATH = FONTPATH + '\\{}'.format(font)
            #assembling query
            if font == arr[-1]:
                fontinfo = "('{}', 0, '{}');".format(font[:-4], directFONTPATH)
            else:
                fontinfo = "('{}', 0, '{}'),".format(font[:-4], directFONTPATH)
            query += fontinfo
        return query

    def searchName(self, fontName):
        query = ("""SELECT * FROM tfonts
            WHERE cfont = '{}';""").format(fontName)
        return query

    #@param fave_bool can be 1 OR 0 or True OR False
    def searchFave(self, fave_bool):
        query = ("""SELECT * FROM tfonts
            WHERE favourite = {};""").format(fave_bool)
        return query
