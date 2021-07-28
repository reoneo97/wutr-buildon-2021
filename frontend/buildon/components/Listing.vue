<template>
    <v-container class="d-flex pa-2">
    <v-sheet v-if="!continued">
        <v-row>
            <h2>{{ saved ? "Edit Listings" : "Listings" }} </h2>
        </v-row>
        <!-- <v-row> -->
    <!-- </div> -->
    <!-- <div>
        <v-content>
        <v-container>
            <v-file-input
            accept="image/png, image/jpeg, image/bmp"
            placeholder="Pick an Image"
            prepend-icon="mdi-camera"
            label="Avatar"
            @change="readURL"
            ></v-file-input>
        </v-container>

        <v-container v-if="originalImg">
            <v-row justify="space-around">
            <v-col cols="5">
                <div class="subheading">Original Image</div>
                <img :src="originalImg"/>
            </v-col>
            <v-col cols="5">
                <div class="subheading">Resized Image</div>
                <img :src="resizedImg"/>
            </v-col>
            </v-row>
        </v-container>
        </v-content>
    </div> -->
    <!-- <div> -->
        <!-- <input id="file-input" type="file" accept="image/*" style="display: none" ref="fileInput" @change="saveImage2($event)" />
        <v-card @click=$refs.fileInput.click()> Pick File </v-card> -->
        <!-- <button @click="uploadImage()"> Upload </button> -->

        <input type="file" accept="image/*" style="display: none" ref="fileInput" @change="saveImage($event)"/>
        <v-card
        v-if="!uploaded"
        class="uploader"
        :color="$vuetify.theme.dark ? 'grey darken-3' : 'grey lighten-4'"
        @click="$refs.fileInput.click()"
        >

            <!-- <imageUploader
                v-if="!uploaded"
                :debug="1"
                :quality="0.7"
                :autoRotate=true
                outputFormat="verbose"
                :preview="true"
                :className="['fileinput', { 'fileinput--loaded' : preview }]"
                :capture="false"
                accept="image/*"
                @input="saveImage"
                :title="itemClass"
                ref="fileInput"
                style="display: none"
            > -->
            <!-- <label for="$refs.fileInput" slot="upload-label"> -->
            <figure v-if="!preview">
                <svg
                xmlns="http://www.w3.org/2000/svg"
                width="80"
                height="80"
                viewBox="0 0 32 32"
                >
                <path
                    class="path1"
                    d="M9.5 19c0 3.59 2.91 6.5 6.5 6.5s6.5-2.91 6.5-6.5-2.91-6.5-6.5-6.5-6.5 2.91-6.5 6.5zM30 8h-7c-0.5-2-1-4-3-4h-8c-2 0-2.5 2-3 4h-7c-1.1 0-2 0.9-2 2v18c0 1.1 0.9 2 2 2h28c1.1 0 2-0.9 2-2v-18c0-1.1-0.9-2-2-2zM16 27.875c-4.902 0-8.875-3.973-8.875-8.875s3.973-8.875 8.875-8.875c4.902 0 8.875 3.973 8.875 8.875s-3.973 8.875-8.875 8.875zM30 14h-4v-2h4v2z"
                ></path>
                </svg>
            </figure>
            <!-- <span v-if="!preview"> Click to upload </span> -->
            <span> {{ preview ? "Preview Image" : "Click to upload" }} </span>
            <!-- </label> -->
            <!-- </imageUploader> -->

            <!-- <v-container v-if="bbox" class='bbox'> -->
                <img v-if="preview" :src="previewImage" class="image-fit">
                    <!-- <VueDraggableResizable :key=b.id :w="b.width" :h="b.height" :parent="true" @dragging="onDrag" @resizing="onResize" class='bbox'>
                        <br>{{ itemClass }}
                        <br> {{ b.x }} x {{ b.y }}
                        <br> {{ b.width }} x {{ b.height }}
                    </VueDraggableResizable> -->

                <!-- <v-hover></v-hover> -->
                <!-- </v-img> -->
                </v-card>
                <v-row v-if="saved">
                    <h3>Listing Name:</h3>
                    <v-text-field v-model="itemName" required :placeholder="itemName" @change="updateItem"/>
                    <!-- <h2>Listing Category:</h2>
                    <v-text-field v-model="itemClass" required :placeholder="itemClass" @change="updateItem"/> -->
                    <span> Select on a listing to change the name </span>
                </v-row>
                <v-row>
                <v-card
                v-if="uploaded"
                class="image-max"
                >
                <img v-if="uploaded" :src="previewImage" class="image-fit">
                    <template v-for="b in bboxes">
                        <VueDragResize @clicked="setActive(b)" :key=b.id :w="b.width" :h="b.height" :parentLimitation="true" @resizing="resize" @dragging="resize" :isDraggable="!saved" :isResizable="!saved" style="border: 2px solid b.color" class="bbox">
                            <p class="d-flex align-start pa-2"> {{ b.class }}
                                <v-spacer/> x
                            </p>
                            <p>{{ b.top }} х {{ b.left }} </p>
                            <p>{{ b.width }} х {{ b.height }}</p>
                        </VueDragResize>
                    </template>
                </v-card>
                </v-row>
                <v-col>
                <v-btn v-if="preview" @click="uploadImage" color="primary"> Upload </v-btn>
                <v-btn v-if="preview" @click="$refs.fileInput.click()" color="grey"><v-card-text> Choose another photo</v-card-text></v-btn>
                </v-col>
          <!-- <progress v-if="uploaded" max="100" :value.prop="uploadPercentage"></progress> -->
        <!-- <vue-draggable-resizable :w="width" :h="height" :parent="true" @dragging="onDrag" @resizing="onResize"> -->

        <!-- </v-container> -->
        <!-- </v-row> -->
        <v-card v-if="saved">

            <!-- list of item names -->
            <v-list>
                <h4>Items</h4>
                <template v-for="(item, i) in items">
                    <v-list-item :key="i">
                        <v-list-item-title v-text="item.Name"></v-list-item-title>
                    </v-list-item>
                    <v-divider :key=i />
                </template>
            </v-list>
        </v-card>
        <v-row>
            <v-col>
            <v-btn v-if="uploaded && !saved" @click="reverse">Back</v-btn>
            <v-btn v-if="uploaded && !saved" @click="addTag">Add tags</v-btn>
            <v-btn v-if="uploaded && !saved" @click="saveTags">Save Tags</v-btn>
            <v-btn v-if="uploaded && saved && !continued" @click="reverse">Back</v-btn>
            <v-btn v-if="uploaded && saved && !continued" @click="saveListings">Save Items</v-btn>
            <v-btn v-if="saved" color="primary" @click="continued=true">Continue</v-btn>
            <!-- <v-btn color="primary" @click="continue = true" nuxt to="/SelectListing">Continue</v-btn> -->
            <v-btn v-if="continued" @click="reverse">Back</v-btn>

            </v-col>
        </v-row>
    </v-sheet>
    <v-sheet v-else>
         <v-row>
            <h2> Select Listings </h2>
        </v-row>
            <v-card>
                <v-icon @click="edit=true">fas fa-edit</v-icon>
                <!-- list of items with categories -->
                <v-list v-if="!edit" flat>
                    <h4>Items</h4>
                    <template v-for="(item, i) in items" >
                        <v-col :key="i">
                    <v-list-item :key="i">
                        <v-list-item-content>
                            <v-list-item-title v-text="item.Name"></v-list-item-title>
                            <v-list-item-subtitle v-text="item.Under"></v-list-item-subtitle>
                            <v-spacer/>
                            <v-list-item-subtitle>${{ item.Price }}</v-list-item-subtitle>
                            <v-switch inset v-model="list" @change="updateItem"></v-switch>
                        </v-list-item-content>
                    </v-list-item>
                        </v-col>
                    <v-divider :key=i />
                    </template>
                </v-list>
                <!-- form -->
                <v-list v-else flat>
                    <v-form>
                        <v-subheader>Edit Items</v-subheader>
                        <v-row v-for="(item, i) in items" :key=i>
                            <v-text-field
                                label="Item Name"
                                v-model="item.Name"
                                required
                            ></v-text-field>
                            <v-text-field
                                label="Item Category"
                                v-model="item.Under"
                                required
                            ></v-text-field>
                        </v-row>
                    </v-form>
                    <v-btn @click="edit=false"> Save </v-btn>
                </v-list>
            </v-card>

        <!-- Earnings Report -->
        <v-row v-if="!edit">
            <h2> Earnings Report </h2>
            <h3> ${{ earnings }} </h3>
            <span>Potential Earnings based on <strong> {{ getListed() }} </strong> items selected</span>
        </v-row>
        <v-row>
            <v-btn @click="listItems"> List Items </v-btn>
        </v-row>
        </v-sheet>
    </v-container>
    <!-- </div> -->
</template>

<script>
import VueDragResize from 'vue-drag-resize';
// import Vue from 'vue'
// import axios from 'axios'
// import VueDraggableResizable from 'vue-draggable-resizable'
// import ImageUploader from 'vue-image-upload-resize'

// Vue.component('vue-draggable-resizable', VueDraggableResizable)
// Vue.component('image-uploader', ImageUploader)
// Vue.use(axios)

// const dataURItoBlob = (dataURI) => {
//   const bytes = dataURI.split(',')[0].indexOf('base64') >= 0
//     ? atob(dataURI.split(',')[1])
//     : unescape(dataURI.split(',')[1]);
//   const mime = dataURI.split(',')[0].split(':')[1].split(';')[0];
//   const max = bytes.length;
//   const ia = new Uint8Array(max);
//   for (let i = 0; i < max; i += 1) ia[i] = bytes.charCodeAt(i);
//   return new Blob([ia], { type: mime });
// };

// const resizeImage = ({ file, maxSize }) => {
//   const reader = new FileReader();
//   const image = new Image();
//   const canvas = document.createElement('canvas');

//   const resize = () => {
//     let { width, height } = image;

//     if (width > height) {
//       if (width > maxSize) {
//         height *= maxSize / width;
//         width = maxSize;
//       }
//     } else if (height > maxSize) {
//       width *= maxSize / height;
//       height = maxSize;
//     }

//     canvas.width = width;
//     canvas.height = height;
//     canvas.getContext('2d').drawImage(image, 0, 0, width, height);

//     const dataUrl = canvas.toDataURL('image/jpeg');

//     return dataURItoBlob(dataUrl);
//   };

//   return new Promise((ok, no) => {
//     if (!file.type.match(/image.*/)) {
//       no(new Error('Not an image'));
//       return;
//     }

//     reader.onload = (readerEvent) => {
//       image.onload = () => ok(resize());
//       image.src = readerEvent.target.result;
//     };

//     reader.readAsDataURL(file);
//   });
// };

export default {
    components: {
        VueDragResize
        // VueDraggableResizable,
        // ImageUploader
    },
    data() {
        return{
            items: [],
            itemName: "Enter the item name",
            itemClass: "Enter the item category",
            activeBox: null,
            bbox: false,
            bboxes: [],
            colors: ['#E97C7A', '#EC917E', '#F2CA89', '#58BA87', '#6DAAC3', '#938DCE'],
            classes: {},
            previewImage:null,
            image: null,
            preview: false, // affects 'add/replace' text
            uploaded: false, // affects upload and tag more btn
            saved: false,
            continued: false,
            list: true,
            edit: false,
            earnings: 0,
            uploadPercentage: 0
        }
    },
    methods: {
        setActive(b) {
            console.log("Setting active box....", b)
            this.activeBox = b;
            this.itemName = b.name;
            this.itemClass = b.class;
        },
        resize(newRect) {
            // console.log(newRect.__ob__.dep.id);
            console.log(this.activeBox)
            // const arr = this.bboxes[this.activeBox.class]
            // console.log(arr)
            let box = this.bboxes[0]
            console.log("Selected box ", box)
            if (this.bboxes.length > 1) {
                console.log("Im here!")
                const index = this.bboxes.map(function(b) { return b.name; }).indexOf(this.activeBox.name);
                box = this.bboxes[index]
                console.log("Found the box: ", box)
            }
            box.width = newRect.width
            box.height = newRect.height
            box.x = newRect.left
            box.y = newRect.top
            // this.width = newRect.width;
            // this.height = newRect.height;
            // this.y = newRect.top;
            // this.x = newRect.left;
            // this.updateBox(this.activeBox, )
        },
        // readURL(file) {
        //     // START: preview original
        //     // you can remove this section if you don't like to preview original image
        //     if (!file.type.match(/image.*/)) {
        //     no(new Error('Not an image'));
        //     return;
        //     }

        //     const reader = new FileReader();
        //     reader.onload = (e) => this.originalImg = e.target.result;
        //     reader.readAsDataURL(file); // convert to base64 string
        //     // END: preview original

        //     // START: preview resized
        //     resizeImage({ file: file, maxSize: 150 }).then((resizedImage) => {
        //     this.resizedImg = URL.createObjectURL(resizedImage);
        //     }).catch((err) => {
        //     console.error(err);
        //     });
        //     // END: preview resized
        // },
        saveImage(output) {
            this.uploaded = false;

            try {
                this.preview = true;
                this.image = output.target.files[0];
                console.log(this.image)
                console.log(output)
                const reader = new FileReader();
                reader.readAsDataURL(this.image);
                reader.onload = output => {
                    this.previewImage = output.target.result;
                    console.log(this.previewImage);
                }
            } catch {
                console.log("error!")
            }

            // this.image = output;
            // console.log(output.dataUrl)
            // this.imageURL = output.dataUrl;
            // const canvas = document.createElement('canvas');
            // const dataUrl = canvas.toDataURL('output.dataUrl');
            // console.log(dataUrl)

            this.bbox = false
            // this.image = event.target.files[0];

            // const reader = new FileReader();
            // this.imageURL = reader.readAsDataURL(this.image.dataUrl);
            // reader.onload = () => {
            //     console.log(this.image);
            // };
        },
        // onResize(x, y, width, height) {
        //     this.x = x
        //     this.y = y
        //     this.width = width
        //     this.height = height
        // },
        // onDrag(x, y) {
        //     this.x = x
        //     this.y = y
        // },
        createTag(x, y, w, h, c, i) {
            const box = {
                'id': i,
                'name': "Item " + i,
                'class': c,
                'left': x,
                'top': y,
                'width': w,
                'height': h,
                'color': this.colors[i]
            }
            if (c in this.classes) {
                box.color = this.classes[c]
            } else {
                this.classes[c] = this.colors[i]
            }
            this.bboxes.push(box)
            console.log("Finished adding! ", this.bboxes)
        },
        addTag() {
            this.createTag(123, 456, 1000, 500, this.itemClass, this.bboxes.length - 1)
        },
        // uploadImage() {
        async uploadImage() {
            this.preview = false
            this.uploaded = true
            // this.bbox = true;
            // const boxes = 3
            // for (let i = 0; i < boxes; i++) {
            //     this.createTag(123, 456, 1000, 500, 'class 1', i)
            // }

            // const postURL = 'http://buildonapp-env.eba-jy7d9spr.ap-southeast-1.elasticbeanstalk.com/listings/img/upload_img'; // upload image
            // const getURL = 'http://buildonapp-env.eba-jy7d9spr.ap-southeast-1.elasticbeanstalk.com/listings/img/info'; // retrieve x,y,w,h, class from ML model
            const data = new FormData();
            data.append('name', "test-image");
            data.append('file', this.image); // contains image data

            const config = {
                header : {
                    // 'Content-Type' : 'image/png'
                    'Content-Type': 'multipart/form-data',
                    // 'Access-Control-Allow-Origin': '*'
               }
            }

            // ,onUploadProgress: function( progressEvent ) {
            //     this.uploadPercentage = parseInt( Math.round( ( progressEvent.loaded / progressEvent.total ) * 100 ));
            // }.bind(this));

            const file = await this.$axios.$post('/api/listings/img/upload_img', data, config);
            // const file = await this.$axios.$post(postURL, data, config);
            console.log("response for upload_img: ", file);
            // this.$axios.$get(getURL + file, {"progress": true}, config).then(res =>
            await this.$axios.$get('/api/listings/img/info/' + file.filename, config).then(res =>
            {
                console.log("response for img/info: ", res);
                this.bbox = true;
                // const boxes = response.boxes
            //     for (let i = 0; i < boxes.length; i++) {
            //         const box = boxes[i]
            //         this.createTag(box.x - box.width/2, box.y + box.height/2, box.width, box.height, box.class, i)
            //         console.log('image upload response > ', response) // response: output from ML model
            //     }
            // })
            // To show client-side: Resized bbox
            }).catch(error => {
                console.log("Failed!!!!")
                console.log(error)
            })
        },
        reverse() {
            if (this.continued) { // to edit listing details
                this.uploaded = true
                this.saved = true
            } else if (this.saved) { // to resize boxes, add or delete tags
                this.uploaded = true
                this.saved = false;
            } else { // to reupload image
                this.image = null;
                this.uploaded = false;
                this.bbox = false;
                this.bboxes = []
            }
        },
        saveTags() {
            // Create list of listings based on the tags
            this.saved = true
            for (let b=0; b < this.bboxes.length; b++) {
                const item = {
                    id: this.bboxes[b].id,
                    'Name': this.bboxes[b].name,
                    'Category': this.bboxes[b].class,
                    'List': this.list
                }
                console.log(this.bboxes[b])
                this.items.push(item)
            }
            console.log("Items after saving")
            console.log(this.items)
        },
        saveListings() {
            // Saves the item that is being edited
            this.continued = true;
            this.uploaded = false;

            // Obtain listing category and price from ML models
            const newItems = []
            for (let i=0; i < this.items.length; i++) {
                // const catURL = 'https://50j0dal2y9.execute-api.ap-southeast-1.amazonaws.com/production/description'
                // let cat = await this.$axios.get(catURL + i.Name)
                // const priceURL = ''
                // let price = await this.$axios.get(priceURL + i.Name)
                // i.Under = cat
                // i.Price = price
                this.items[i].Under = "Placeholder Category";
                this.items[i].Price = 100;
                newItems.push(this.items[i])
            }
            console.log(newItems)
            this.items = newItems
            this.earnings = this.items.map(function(i) { return i.Price }).reduce((a, b) => a + b, 0);
        },
        updateItem() {
            const index = this.items.map(function(i) { return i.id; }).indexOf(this.activeBox.id);
            this.items[index].Name = this.activeBox.name;
            // this.items[index].Category = this.activeBox.class;
            this.items[index].List = this.list;
            this.earnings = this.items.map(function(i) { return i.Price }).reduce((a, b) => a + b, 0);
        },
        getListed() {
            const listed = this.items.filter(function (i) {
                return i.list
            });
            return listed.length
        },
        listItems() {

        }
    }
    // watch: {
    //     box() {
    //         this.
    //     }
    // }
}
</script>

<style scoped>

.container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;

/* box-sizing: border-box;
    border: 2px solid rgb(56, 206, 226); */
}

.uploader {
    box-sizing: border-box;
    border: 2px solid #6c6c6c;
    padding: 8%;
    margin-inline:25%;

    /* margin-right: 15%;
    margin-left: 15%;
    width: auto;
    height: auto; */
}

.bbox {
    box-sizing: border-box;
    border: 2px solid #6c6c6c;
}

.row {
    /* box-sizing: border-box;
    border: 2px solid rgb(93, 179, 90); */

    justify-content: center;
    align-content: center;
    padding: 30px;
}

.footer {
    /* justify-content: center; */

    /* align-items: stretch; */
    box-sizing: border-box;
    padding: 10px;
    border: 2px solid rgb(195, 0, 259);
}

.image-max {
    margin-inline: 25%;
}

.image-fit {
    height: 100%;
    width: 100%;
    object-fit: cover;
}

 </style>
