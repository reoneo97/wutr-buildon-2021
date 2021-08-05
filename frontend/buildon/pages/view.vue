<template>
    <v-icon v-if="!loaded"> fas fa-circle-notch fa-spin
    </v-icon>
    <!-- <v-container v-if="!loaded">
        <template v-slot:loader>
            <span>Loading...</span>
        </template>
    </v-container> -->
        <v-container v-else>
    <!-- <v-row v-if="loaded"> -->
    <h2> View Item

 <!-- v-bind:itemName.sync="itemName"> -->
    </h2>
    <!-- <v-row> -->
        <v-col class="d-flex justify-space-between">
        <v-card @update-itemName="loadItem" max-width="450px">
            <img :src="`https://wutr-images2.s3.ap-southeast-1.amazonaws.com/${item.filename}`" class="image-fit" >
            <v-hover>
            </v-hover>
        </v-card>
        <v-card min-width="650px">
            <!-- <div class="icon">
                <v-btn fab small dark color="grey">
                    <v-icon>mdi-account</v-icon>
                </v-btn>
                </div>Seller
                <v-spacer/>
                <v-btn color="red" dark> Chat </v-btn>

            <table class="table-styles">
                <thead>
                    <tr>
                        <th id="h1"> Item </th>
                        <th id="h1"> Description </th>
                        <th id="h1"> Price </th>
                        <th id="h1"> For Sale </th>
                    </tr>
                </thead>
                <tbody>
                    <template v-for="(listing, i) in item.listings">
                        <td :key=i> {{ listing.name }} </td>
                        <td :key=i> {{ listing.description }} </td>
                        <td :key=i> {{ listing.price }} </td>
                        <td :key=i> {{ listing.for_sale }} </td>
                    </template>
                </tbody>
            </table> -->
            <v-list>
                <v-list-item>
                <div class="icon">
                <v-btn fab small dark color="grey">
                    <v-icon>mdi-account</v-icon>
                </v-btn>
                </div>seller123
                <v-spacer/>
                <v-btn color="red" dark> Chat </v-btn>
                </v-list-item>
                <v-divider/>
                <!-- <h4>Items</h4>
                <v-divider/> -->
                <v-list-item>
                <!-- <v-col> -->
                    <v-list-item-title class="btn2"><b>Item</b></v-list-item-title>
                    <v-card min-width="350px" elevation="0">
                    <v-list-item-title class="btn2"><b>Description</b></v-list-item-title>
                    </v-card>
                    <v-list-item-title><b>Price</b></v-list-item-title>
                    <v-list-item-title><b>For Sale</b></v-list-item-title>
                    <!-- <v-divider></v-divider> -->
                    <!-- <v-list-item-title>Select</v-list-item-title> -->
                    <!-- <h4>Item</h4>
                    <h4>Category</h4>
                    <h4>Price</h4><br>
                    <h4>Select</h4> -->
                <!-- </v-col> -->
                </v-list-item>
                <template v-for="(listing, i) in item.listings">
                <!-- <v-list-item-group> -->
                <v-divider :key=i />
                <v-list-item :key="i">
                    <v-list-item-title v-text="listing.name" class="icon"></v-list-item-title>
                    <v-card min-width="350px" elevation="0">
                    <v-list-item-title v-text="listing.description"></v-list-item-title>
                    </v-card>
                    <v-list-item-title>${{listing.price}}</v-list-item-title>
                    <v-switch disabled inset v-model="listing.for_sale"></v-switch>
                <!-- </v-card> -->
                    <!-- <v-list-item-title v-text="listing.for_sale ? `For Sale` : `Not for Sale`"></v-list-item-title> -->
                </v-list-item>

                <!-- </v-list-item-group> -->
                    <!-- <v-btn v-if="listing.for_sale" color="red" dark> Chat </v-btn> -->
                </template>
                <v-divider />
                <!-- </template> -->
            </v-list>
            <!-- <div class="btn">
            <v-btn color="red" dark> Chat </v-btn>
            </div> -->
        </v-card>
    </v-col>
  <!-- </v-row> -->
<!-- </v-row> -->
    </v-container>
    <!-- </v-col> -->
</template>

<script>
export default {
    data() {
        return {
            filname: "",
            item: {},
            loaded: false
        };
    },
    // async mounted() {
    mounted() {
        console.log("Im mounting....")
        this.filename = this.filename ? this.filename : '14c6e92bf46311eb990b80fa5b6197fb.jpeg'
        console.log(this.filename)
        this.loadItem(this.filename.split(".")[0])
    //     // const URL = 'http://wutr-staging.eba-jy7d9spr.ap-southeast-1.elasticbeanstalk.com/api/users/feed?limit=20'
    //     // const URL = '/api/users/feed/?limit=20'
    //     this.item = await this.$axios.$get('/api/listings/' + this.itemName)
    //     console.log(this.item)
    },
    methods: {
        async loadItem(itemid) {
            console.log("Im loading....")
            await this.$axios.$get('/api/listings/create' + itemid).then(res => {
                this.item = res
                console.log(this.item)
                this.loaded = true
            }).catch(error => {
                console.log(error)
                this.loaded = true
                this.item = {
                    "id": "string",
                    "filename": this.filename,
                    "listings": [
                        {
                            "name": "item name",
                            "description": "this is an item description that is very very very very very long",
                            "price": 100,
                            "for_sale": false,
                            "tags": [],
                            "bbox": {
                                "cls": "class",
                                "x": 0,
                                "y": 0,
                                "w": 0,
                                "h": 0
                            }
                        },
                        {
                            "name": "item 2 name",
                            "description": "this is another item description that is even more more more more longer",
                            "price": 200,
                            "for_sale": true,
                            "tags": [],
                            "bbox": {
                                "cls": "class",
                                "x": 0,
                                "y": 0,
                                "w": 0,
                                "h": 0
                            }
                        }
                    ],
                    "user": "string"
                }
            })
            console.log(this.item)
        }
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

.btn { 
    padding: 30px;
}

.icon {
    padding: 10px;
}

.btn2 {
    margin-inline: 4%
}
</style>