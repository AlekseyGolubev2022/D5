from news.models import *;
user1 = User.objects.create_user('user0001');
user2 = User.objects.create_user('user0002');
user3 = User.objects.create_user('user0003');
Author.objects.create(user=user1); 
Author.objects.create(user=user2);
Category.objects.create(name='Category1');
Category.objects.create(name='Category2');
Category.objects.create(name='Category3');
Category.objects.create(name='Category4');
cat1=Category.objects.get(name='Category1'); 
cat2=Category.objects.get(name='Category2'); 
cat3=Category.objects.get(name='Category3'); 
cat4=Category.objects.get(name='Category4'); 
instance1 = Post.objects.create(title='Статья00001',genre='A',author=user1.author,text='00001 текст...');
instance1.categories.set((cat1,cat2));
instance2 = Post.objects.create(title='Статья00002',genre='A',author=user2.author,text='00002 текст...');
instance2.categories.set((cat3,));
instance3 = Post.objects.create(title='Новость00003',genre='N',author=user2.author,text='00003 текст...');
instance3.categories.set((cat4,));
comment1 = Comment.objects.create(post=instance1,author=user2,text='Коммент1');
comment2 = Comment.objects.create(post=instance1,author=user3,text='Коммент2');
comment3 = Comment.objects.create(post=instance2,author=user1,text='Коммент3');
comment4 = Comment.objects.create(post=instance3,author=user1,text='Коммент4');

instance1.like();instance1.like();instance1.dislike();
instance2.like();instance2.like();instance2.dislike();
instance3.like();instance3.like();instance3.dislike();
comment1.like();comment1.like();comment1.dislike();
comment2.like();comment2.like();comment2.dislike();
comment3.like();comment3.like();comment3.dislike();
comment4.like();comment4.like();comment4.dislike();
user1.author.update_rating(); # user1.author.rating
user2.author.update_rating(); # user2.author.rating
