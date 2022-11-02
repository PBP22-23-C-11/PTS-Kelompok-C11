class SortBy:
    DATE_ASC = 'date_asc'
    DATE_DESC = 'date_desc'
    LIKES_ASC = 'likes_asc'
    LIKES_DESC = 'likes_desc'
    
    VALUES = (DATE_ASC, DATE_DESC, LIKES_ASC, LIKES_DESC)
    
    def convert(string):
        if string not in SortBy.VALUES:
            raise Exception('Invalid string')
        
        if string[len(string)-4:] == '_asc':
            direction = ''
            string = string[:len(string)-4]
        else:
            direction = '-'
            string = string[:len(string)-5]
        
        if string == 'date':
            string = 'created_at'
        
        middle = 'article__'
        if string == 'likes':
            middle = ''
        
        return direction + middle + string

class Category:
    UMKM = 'umkm'
    SUBSCRIBED = 'subscribed'
    OFFICIAL = 'official'
    
    VALUES = (UMKM, SUBSCRIBED, OFFICIAL)

class UMKMType:
    NONE = None
    USERNAME = 'username'
    NAME = 'name'
    
    VALUES = (NONE, USERNAME, NAME)