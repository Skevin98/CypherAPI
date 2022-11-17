from API.serializers import ArticleSerializer,AuthorSerializer,MediaSerializer, \
    ArticleDetailSerializer, AuthorDetailSerializer, MediaDetailSerializer, \
    AuthorAdminSerializer, AuthorAdminDetailSerializer, ArticleAdminSerializer, \
    ArticleAdminDetailSerializer
from API.models import Author,Article,Media
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from url_filter.integrations.drf import DjangoFilterBackend


class MultipleSerializerMixin:

    detail_serializer_class = None
    

    def get_serializer_class(self):
        if (self.action == 'retrieve' or self.action == "create")  and self.detail_serializer_class is not None:
            return self.detail_serializer_class  
        return super().get_serializer_class()


class AuthorViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet):
    detail_serializer_class = AuthorDetailSerializer
    serializer_class = AuthorSerializer

    def get_queryset(self):
        return Author.objects.filter(active=True)


    


class ArticleViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet):
    detail_serializer_class = ArticleDetailSerializer
    serializer_class = ArticleSerializer


    def get_queryset(self):
        return Article.objects.filter(active=True)
    


class MediaViewSet(MultipleSerializerMixin,ReadOnlyModelViewSet):
    detail_serializer_class = MediaDetailSerializer
    serializer_class = MediaSerializer

    def get_queryset(self):
        return Media.objects.filter(active=True)




####################### Admin ViewSets ###############################


class AuthorAdminViewSet(MultipleSerializerMixin, ModelViewSet):
    detail_serializer_class = AuthorAdminDetailSerializer
    serializer_class = AuthorAdminSerializer

    def get_queryset(self):
        return Author.objects.all()

    @action(detail=True,methods=['post','get'])
    def disable(self, request, pk):
        author = self.get_object()
        author.active = False
        author.save()

        author.articles.filter(author = author).update(active = False)

        return Response()

    @action(detail=True,methods=['post','get'])
    def enable(self, request, pk):
        author = self.get_object()
        author.active = True
        author.save()

        return Response()


class ArticleAdminViewSet(MultipleSerializerMixin, ModelViewSet):
    detail_serializer_class = ArticleAdminDetailSerializer
    serializer_class = ArticleAdminSerializer


    def get_queryset(self):
        return Article.objects.all()

    @action(detail=True,methods=['post','get'])
    def disable(self, request, pk):
        article = self.get_object()
        article.active = False
        article.save()


        return Response()

    @action(detail=True,methods=['post','get'])
    def enable(self, request, pk):
        article = self.get_object()
        article.active = True
        article.save()

        return Response()
    


class MediaAdminViewSet(MultipleSerializerMixin,ModelViewSet):
    detail_serializer_class = MediaDetailSerializer
    serializer_class = MediaSerializer

    def get_queryset(self):
        return Media.objects.all()

    @action(detail=True,methods=['post','get'])
    def disable(self, request, pk):
        media = self.get_object()
        media.active = False
        media.save()


        return Response()

    @action(detail=True,methods=['post','get'])
    def enable(self, request, pk):
        media = self.get_object()
        media.active = True
        media.save()

        return Response()