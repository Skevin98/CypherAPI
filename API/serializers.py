from rest_framework import serializers
from API.models import Author, Article, Media



class ArticleSerializer(serializers.ModelSerializer):
    
    author = serializers.SerializerMethodField()
    co_authors = serializers.SerializerMethodField()


    class Meta:
        model = Article
        fields = ['id','title','description','publish_date','article_type'
        ,'author','co_authors','active','content','header_img']

    def get_author(self, instance):
        query = instance.author
        serializer = AuthorInfoSerializer(query)
        return serializer.data

    def get_co_authors(self, instance):
        query = instance.co_authors.filter(active = True)
        serializer = AuthorInfoSerializer(query, many = True)
        return serializer.data


class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = ['id','title','publish_date','media_type','active','file']


class AuthorSerializer(serializers.ModelSerializer):

    # articles = ArticleSerializer(many = True)
    articles = serializers.SerializerMethodField()

    def get_articles(self, instance):

        queryset = instance.articles.filter(active = True)
        serializer = ArticleSerializer(queryset, many = True)
        return serializer.data

    class Meta:
        model = Author
        fields = ['id','username','description','articles', 'profile_img']

class AuthorInfoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Author
        fields = ['id','username','description', 'profile_img','active']


#############        Detail Serializers          ###################


class AuthorDetailSerializer(serializers.ModelSerializer):

    articles = serializers.SerializerMethodField()
    # articles = ArticleSerializer(many = True)

    class Meta:
        model = Author
        fields = ['id','user','username','description','profile_img',
        'active','articles']

    def get_articles(self, instance):

        queryset = instance.articles.filter(active = True)
        serializer = ArticleSerializer(queryset, many = True)
        return serializer.data

class ArticleDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    co_authors = serializers.SerializerMethodField()

    # author = AuthorInfoSerializer()
    # co_authors = AuthorInfoSerializer(many=True)
    

    class Meta:
        model = Article
        fields = ['id','title','publish_date','update_date','description',
        'tag','active','content','author','co_authors','article_type','header_img']

    def get_author(self, instance):
        query = instance.author
        serializer = AuthorInfoSerializer(query)
        return serializer.data

    def get_co_authors(self, instance):
        query = instance.co_authors.filter(active = True)
        serializer = AuthorInfoSerializer(query, many = True)
        return serializer.data


class MediaDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = ['id','title','publish_date','update_date','description',
        'tag','active','media_type','file']

######### Admin serializer ################


class AuthorAdminSerializer(serializers.ModelSerializer):

    articles = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id','username','description','articles', 'profile_img', 'active']

    def get_articles(self, instance):

        queryset = instance.articles.all()
        serializer = ArticleSerializer(queryset, many = True)
        return serializer.data


class ArticleAdminSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Article
        fields = ['id','title','publish_date','article_type'
        ,'author','co_authors','active','content','header_img']

class ArticleAdminDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    co_authors = serializers.SerializerMethodField()

    # author = AuthorInfoSerializer()
    # co_authors = AuthorInfoSerializer(many=True)
    

    class Meta:
        model = Article
        fields = ['id','title','publish_date','update_date','description',
        'tag','active','content','author','co_authors','article_type','header_img']

    def get_author(self, instance):
        query = instance.author
        serializer = AuthorInfoSerializer(query)
        return serializer.data

    def get_co_authors(self, instance):
        query = instance.co_authors
        serializer = AuthorInfoSerializer(query, many = True)
        return serializer.data


class AuthorAdminDetailSerializer(serializers.ModelSerializer):

    articles = serializers.SerializerMethodField()
    # articles = ArticleSerializer(many = True)

    class Meta:
        model = Author
        fields = ['id','user','username','description','profile_img',
        'active','articles']

    def get_articles(self, instance):

        queryset = instance.articles.all()
        serializer = ArticleAdminSerializer(queryset, many = True)
        return serializer.data