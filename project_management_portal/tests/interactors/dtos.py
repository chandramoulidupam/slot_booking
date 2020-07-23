from datetime import datetime
import factory
from gyaan.interactors.storages.dtos import UserDTO, PostDTO

class UserDTOFactory(factory.Factory):

    class Meta:
        model = UserDTO

    user_id = factory.Sequence(lambda n: '%d' %n)
    name = factory.Sequence(lambda n: 'user%d' %n)


class TagDTOFactory:

    class Meta:
        model = TagDTOFactory

    tag_id = factory.Sequence(lambda n: '%d' %n)
    name = factory.Sequence(lambda n: 'tag%d' %n)


class PostTagDTOFactory:

    class Meta:
        model = PostTagDTOFactory

    post_id = factory.Sequence(lambda n: '%d' %n)
    tag_id = factory.Sequence(lambda n: '%d' %n)


class PostTagDetailsDTOFactory:

    class Meta:
        model = PostTagDetailsDTOFactory

    tags = factory.SubFactory(TagDTOFactory)
    post_tag_ids = factory.SubFactory(PostTagDTOFactory)


class PostDTOFactory(factory.Factory):

    class Meta:
        model = PostDTO

    post_id = factory.Sequence(lambda n: '%d' %n)
    title = factory.Sequence(lambda n: 'title%d' %n)
    description = factory.Sequence(lambda n: 'descriptionx%d' %n)
    posted_at = factory.LazyAttribute(lambda t: datetime.now())
    posted_by = factory.SubFactory(UserDTOFactory)


class PostReactionsCountDTO:

    class Meta:
        model = PostReactionsCountDTO

    post_id = factory.Sequence(lambda n: '%d' %n)
    reactions_count = factory.Sequence(lambda n: '%d' %n)


class CommentDTOFactory:

    class Meta:
        model = CommentDTOFactory

    comment_id = factory.Sequence(lambda n: '%d' %n)
    commented_by = factory.Sequence(lambda n: '%d' %n)
    commented_at = factory.Sequence(lambda n: '%d' %n)
    commented_content = factory.Sequence(lambda n: '%d' %n)


class CommentRepliesCountDTOFactory:

    class Meta:
        model = CommentRepliesCountDTOFactory

    comment_id = factory.Sequence(lambda n: '%d' %n)
    replies_count = factory.Sequence(lambda n: '%d' %n)


class CommentReactionsCountFactory:

    class Meta:
        model = CommentReactionsCountFactory

    comment_id = factory.Sequence(lambda n: '%d' %n)
    reactions_count = factory.Sequence(lambda n: '%d' %n)
