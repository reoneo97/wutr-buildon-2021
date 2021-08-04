<template>
    <v-row>
    <v-header @update-itemName="itemName = $event">
 <!-- v-bind:itemName.sync="itemName"> -->
    </v-header>
    <v-row>
        <v-col>
        <v-card>
            <img :src="`https://wutr-images2.s3.ap-southeast-1.amazonaws.com/${item.image}`" class="image-fit" >
        </v-card>
        <v-card>
            <v-list>
                <h4>Items</h4>
                <!-- <template v-for="(item, i) in items"> -->
                <v-list-item v-for="(listing, i) in item.listings" :key="i" @click="setActive(item)">
                    <v-divider :key=i />
                    <v-list-item-title v-text="listing.name"></v-list-item-title>
                    <v-list-item-title v-text="listing.description"></v-list-item-title>
                    <v-list-item-title v-text="listing.price"></v-list-item-title>
                    <v-list-item-title v-text="listing.for_sale ? `For Sale` : `Not for Sale`"></v-list-item-title>
                    <v-btn v-if="listing.for_sale" color="red" dark> Chat </v-btn>
                </v-list-item>
                <!-- </template> -->
            </v-list>

        </v-card>
    </v-col>
  </v-row>
</v-row>
</template>

<script>
export default {
    data() {
        return {
            itemName: "",
            item: {},
        };
    },
    async mounted() {
        // const URL = 'http://wutr-staging.eba-jy7d9spr.ap-southeast-1.elasticbeanstalk.com/api/users/feed?limit=20'
        // const URL = '/api/users/feed/?limit=20'
        this.item = await this.$axios.$get('/api/listings/' + this.itemName)
        console.log(this.item)
    }
}
</script>

<style scoped>
.row {
    justify-content: center;
    align-content: center;
    padding: 30px;
}

.image-fit {
    height: 100%;
    width: 100%;
    object-fit: cover;
}

</style>