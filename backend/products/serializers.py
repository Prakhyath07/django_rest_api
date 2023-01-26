from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    ## to change the name from get_discount to my_discount
    my_discount = serializers.SerializerMethodField(read_only= True)
    edit_url = serializers.SerializerMethodField(read_only= True)

    ## prefered way to get url
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field = 'pk'
    )

    class Meta:
        model = Product

        fields = [
            'url',
            'email',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def create(self, validated_data):
        email=validated_data.pop('email')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        email=validated_data.pop('email')
        return super().update(instance, validated_data)

    def get_my_discount(self, obj):
        ## checking id the object passed is an instance of model or not
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

    def get_edit_url(self,obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-update", kwargs={"pk":obj.pk}, request= request)
        