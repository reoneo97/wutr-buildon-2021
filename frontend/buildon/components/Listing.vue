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
                    <v-text-field v-model="itemName" placeholder="Select on an item to change its name" label="Listing Name"/>
                    <v-btn @click="updateItem"> Save Edit </v-btn>
                    <!-- <h2>Listing Category:</h2>
                    <v-text-field v-model="itemClass" required :placeholder="itemClass" @change="updateItem"/> -->
                </v-row>
                <v-row>
                <v-card
                v-if="uploaded"
                class="image-max"
                >
                <img v-if="uploaded" :src="previewImage" class="image-fit">
                    <template v-for="b in bboxes">
                        <VueDragResize @clicked="setActive(b)" :key=b.id :w="b.width" :h="b.height" :y="b.top" :x="b.left" :parentLimitation="true" @resizing="resize" @dragging="resize" :isDraggable="!saved" :isResizable="!saved" :style="getStyle(b)">
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
                <ProgressBar v-if="uploaded && uploadPercentage != 100 && !saved" :options="options" :value="uploadPercentage"/>
                <!-- <prog></prog> -->
                <!-- <prog
                    :data="circles"
                    :progress="uploadPercentage"
                    :angle="-90"
                    color="blue"
                    :colorFill="colorFillGradient"
                    emptyColor="#8ec5fc"
                    :emptyColorFill="emptyColorFillGradient"
                    :size="300"
                    :thickness="10"
                    emptyThickness="10%"
                    lineMode="in 10"
                    :legend="true"
                    :legendValue="180"
                    legendClass="legend-custom-style"
                    dash="60 0.9"
                    animation="reverse 700 400"
                    :noData="false"
                    :loading="false"
                    fontColor="white"
                    :half="false"
                    :gap="10"
                    dot="10 blue"
                    fontSize="5rem">

                    <span slot="legend-value">/100%</span>
                    <p slot="legend-caption">GOOD JOB</p>

                    </prog> -->
            <!-- <VueProgressBar></VueProgressBar> -->
          <!-- <progress v-if="uploaded" max="100" :value.prop="uploadPercentage"></progress> -->

        <!-- <vue-draggable-resizable :w="width" :h="height" :parent="true" @dragging="onDrag" @resizing="onResize"> -->

        <!-- </v-container> -->
        <!-- </v-row> -->
        <v-card v-if="saved">

            <!-- list of item names -->
            <v-list>
                <h4>Items</h4>
                <!-- <template v-for="(item, i) in items"> -->
                    <v-list-item-group color="primary" v-model="selectedItem">
                    <v-list-item v-for="(item, i) in bboxes" :key="i" @click="setActive(item)">
                        <v-divider :key=i />
                        <v-list-item-title v-text="item.name"></v-list-item-title>
                    </v-list-item>
                    </v-list-item-group>
                <!-- </template> -->
            </v-list>
        </v-card>
        <v-row>
            <v-col>
            <v-btn v-if="uploaded && !saved" @click="reverse">Back</v-btn> <!-- back to upload image page -->
            <v-btn v-if="uploaded && !saved" @click="addTag">Add tags</v-btn>
            <v-btn v-if="uploaded && !saved" color="primary" @click="saveTags">Save Tags</v-btn> <!-- cont to edit listings page -->
            <v-btn v-if="uploaded && saved && !continued" @click="reverse">Back</v-btn> <!-- back to adjusting tags -->
            <v-btn v-if="uploaded && saved && !continued" color="primary" @click="saveListings">Save Items</v-btn> <!-- cont to earnings page -->
            <v-btn v-if="saved && continued" color="primary" @click="continued=true">Continue</v-btn>
            <!-- <v-btn color="primary" @click="continue = true" nuxt to="/SelectListing">Continue</v-btn> -->
            <v-btn v-if="continued" @click="reverse">Back</v-btn> <!-- back to listings page -->

            </v-col>
        </v-row>
    </v-sheet>
    <v-sheet v-else>
         <v-row>
            <h2> Select Listings </h2>
        </v-row>
            <v-card>
                <div class="btn">
                <v-btn @click="edit=true" v-if="!edit">
                <v-icon>mdi-pencil</v-icon>
                </v-btn>
                </div>
                <!-- list of items with categories -->
                <v-list v-if="!edit" flat>
                    <!-- <h4>Items</h4> -->
                    <v-card elevation="0" max-width="1090px">
                <v-list-item>
                <!-- <v-col> -->
                    <v-list-item-title class="font-weight-black">Item</v-list-item-title>
                    <v-list-item-title class="font-weight-black">Category</v-list-item-title>
                    <v-list-item-title class="font-weight-black">Price</v-list-item-title>
                    <!-- <v-divider></v-divider> -->
                    <!-- <v-list-item-title>Select</v-list-item-title> -->
                    <!-- <h4>Item</h4>
                    <h4>Category</h4>
                    <h4>Price</h4><br>
                    <h4>Select</h4> -->
                <!-- </v-col> -->
                </v-list-item>
                    </v-card>
                    <template v-for="(item, i) in bboxes" >
                    <v-divider :key=i />
                        <!-- <v-row :key="i"> -->
                    <v-list-item :key="i">
                        <!-- <v-col :key="i"> -->
                        <!-- <v-list-item-content> -->
                            <v-list-item-title v-text="item.name"></v-list-item-title>
                            <v-list-item-title v-text="item.under"></v-list-item-title>
                            <v-list-item-title>${{ item.price }}</v-list-item-title>
                        <!-- </v-list-item-content> -->
                        <v-switch inset v-model="item.list" @change="updateListing(item)"></v-switch>
                        <!-- </v-col> -->
                    </v-list-item>
                        <!-- </v-row> -->
                    </template>
                </v-list>
                <!-- form -->
                <v-list v-else flat>
                <div class="btn">
                    <v-btn @click="editListing"> Cancel </v-btn>
                </div>
                    <v-form>
                        <v-subheader>Edit Items</v-subheader>
                        <v-row v-for="(item, i) in bboxes" :key=i>
                            <v-col>
                            <h4>Item {{ i + 1 }}:</h4>
                            <v-text-field
                                label="Item Name"
                                v-model="item.name"
                                required
                            ></v-text-field>
                            <v-text-field
                                label="Item Category"
                                v-model="item.under"
                                required
                            ></v-text-field>
                            <v-text-field
                                label="Item Price"
                                v-model="item.price"
                                required
                            ></v-text-field>
                            </v-col>
                        </v-row>
                    </v-form>
                    <v-btn @click="editListing" color="primary"> Save </v-btn>
                </v-list>
            </v-card>

        <!-- Earnings Report -->
        <v-row v-if="!edit">
            <h2> Earnings Report </h2>
          <apexchart v-if="continued" width="380" type="radialBar" :options="chartOptions" :series="series"></apexchart>
            <v-col>
            <!-- <h3> ${{ earnings }} </h3> -->
            <!-- <span>Potential Earnings based on <strong> {{ listedCount() }} </strong> items selected</span> -->
            </v-col>
        </v-row>
        <v-col v-if="!edit">
            <v-btn @click="reverse"> Back </v-btn>
            <v-btn @click="listItems" color="primary"> List Items </v-btn>
        </v-col>
        </v-sheet>
    </v-container>
    <!-- </div> -->
</template>

<script>
// import Vue from 'vue';
import VueDragResize from 'vue-drag-resize';
// import Chartkick from 'vue-chartkick'
// import Chart from 'chart.js'
import VueApexCharts from 'vue-apexcharts'
// import VueEllipseProgress from 'vue-ellipse-progress';
import ProgressBar from 'vuejs-progress-bar'
// import VueProgressBar from 'vue-progress-bar';

// Vue.use(Chartkick.use(Chart))

// Chartkick.options = {
//   colors: ['#A52A2A', '#D3D3D3']
// }
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
// Vue.use(VueApexCharts)

// Vue.component('apexchart', VueApexCharts)

export default {
    components: {
        VueDragResize,
        apexchart: VueApexCharts,
        ProgressBar
        // prog: VueEllipseProgress,
        // VueProgressBar
        // VueDraggableResizable,
        // ImageUploader
    },
    data() {
        return{
            // items: [],
            itemName: "Select on an item in the list to change its name",
            itemClass: "Enter the item category",
            activeBox: null,
            bbox: false,
            bboxes: [],
            colors: ['#b32d00', '#6DAAC3', '#ffaa00', '#58BA87', '#e67300', '#938DCE'],
            classes: {},
            previewImage:null,
            image: null,
            filename: '',
            preview: false, // affects 'add/replace' text
            uploaded: false, // affects upload and tag more btn
            saved: false,
            continued: false,
            list: true,
            edit: false,
            earnings: 0,
            total: 1000,
            uploadPercentage: 0,
            selectedItem: 0,
            options: {
                text: {
                    color: '#FFFFFF',
                    shadowEnable: true,
                    shadowColor: '#000000',
                    fontSize: 14,
                    fontFamily: 'Helvetica',
                    dynamicPosition: false,
                    hideText: false
                },
                progress: {
                    color: '#2dbd2d',
                    backgroundColor: '#333333',
                    inverted: false
                },
                layout: {
                    height: 35,
                    width: 140,
                    verticalTextAlign: 61,
                    horizontalTextAlign: 43,
                    zeroOffset: 0,
                    strokeWidth: 30,
                    progressPadding: 0,
                    type: 'line' // or circular
                }
            },
            series: [],
            chartOptions: {
                chart: {
                    height: 350,
                    type: 'radialBar',
                },
                plotOptions: {
                    radialBar: {
                        hollow: {
                            size: ""
                            // size: `${this.earnings/this.total}%`,
                        }
                    },
                },
                labels: ['Earnings Report'],
            },
            // series: [this.earnings, this.total-this.earnings]
            // options: {
            //     chart: {
            //     id: 'vuechart-example'
            //     },
            //     xaxis: {
            //     categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998]
            //     }
            // },
            // series: [{
            //     name: 'series-1',
            //     data: [30, 40, 45, 50, 49, 60, 70, 91]
            // }]
        }
    },
    methods: {
        setActive(b) {
            console.log("Setting active box....", b)
            this.activeBox = this.bboxes[b.id];
            this.itemName = b.name;
            this.itemClass = b.class;
            this.selectedItem = b.id
        },
        resize(newRect) {
            // console.log(newRect.__ob__.dep.id);
            // const arr = this.bboxes[this.activeBox.class]
            // console.log(arr)
            // let box = this.bboxes[this.activeBox.id]
            console.log("Selected box ", this.activeBox)
            // if (this.bboxes.length > 1) {
            //     const index = this.bboxes.map(function(b) { return b.name; }).indexOf(this.activeBox.name);
            //     box = this.bboxes[index]
            //     console.log("Found the box: ", box)
            // }
            const index = this.activeBox.id
            // const box = this.bboxes[index]
            this.bboxes[index].width = newRect.width
            this.bboxes[index].height = newRect.height
            this.bboxes[index].left = newRect.left
            this.bboxes[index].top = newRect.top
            // console.log(`Changed box: ${box}`)
            // console.log(box)
            // this.bboxes[index] = box
            console.log(`Saved box: ${this.bboxes[index]}`)
            console.log(this.bboxes[index])
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
            const index = this.bboxes.length
            this.createTag(0, 0, 100, 50, `class ${index}`, index)
        },
        getStyle(box) {
            const boxStyle = {
                "box-sizing": `border-box`,
                "border": `2px solid ${box.color}`
            };
            return boxStyle;
        },
        uploadImage() {
        // async uploadImage() {
            this.preview = false
            this.uploaded = true
            // const postURL = 'http://buildonapp-env.ebsa-jy7d9spr.ap-southeast-1.elasticbeanstalk.com/listings/img/upload_img'; // upload image
            // const getURL = 'http://buildonapp-env.eba-jy7d9spr.ap-southeast-1.elasticbeanstalk.com/listings/img/info'; // retrieve x,y,w,h, class from ML model
            const data = new FormData();
            data.append('name', "test-image");
            data.append('file', this.image); // contains image data

            console.log("Data for upload_img")
            console.log(data)
            // const config = {
            //     onUploadProgress: function( progressEvent ) {
            //         this.uploadPercentage = parseInt( Math.round( ( progressEvent.loaded / progressEvent.total ) * 100 ));
            //     }.bind(this)
            // }

            const file = 'res'
            // const file = await this.$axios.$post('/listings/img/upload_img', data);
            this.filename = file
            // const file = await this.$axios.$post('/api/listings/img/upload_img', data, config);
            // const file = await this.$axios.$post(postURL, data);
            console.log("response for upload_img: ", file);
            // this.$axios.$get(getURL + file, {"progress": true}).then(res =>
            // this.waiting = true
            // this.$Progress.start()
            this.bbox = true;
            const boxes = 3
            for (let i = 0; i < boxes; i++) {
                this.createTag(0, 0, 100, 50, `class ${i}`, i)
            }
            // await this.$axios.$get('/listings/img/info/' + file.filename, config).then(res =>
            // {
            //     console.log("response for img/info: ", res);
            //     this.bbox = true;
            //     // const boxes = 3
            //     for (let i = 0; i < boxes; i++) {
            //         this.createTag(0, 0, 100, 50, `class ${i}`, i)
            //     }
            //     // const boxes = response.boxes
            // //     for (let i = 0; i < boxes.length; i++) {
            // //         const box = boxes[i]
            // //         this.createTag(box.x - box.width/2, box.y + box.height/2, box.width, box.height, box.class, i)
            // //         console.log('image upload response > ', response) // response: output from ML model
            // //     }
            // // })
            // // To show client-side: Resized bbox
            // }).catch(error => {
            //     console.log("Failed!!!!")
            //     console.log(error)
            // })
            // this.$Progress.finish()

        },
        reverse() {
            if (this.continued) { // to edit listing details
                this.continued = false
                this.saved = true
                this.uploaded = true
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
            this.bboxes.map(b => {
                b.list = this.list
                return b
            })
            // for (let b=0; b < this.bboxes.length; b++) {
            //     this.bboxes[b]['list'] = this.list
            // }
            console.log("Items after saving")
            console.log(this.bboxes)
        },
        saveListings() {
        // async saveListings() {
            // Saves the item that is being edited
            this.continued = true;
            this.uploaded = false;

            // Obtain listing category and price from ML models
            // const newItems = []
            for (let i=0; i < this.bboxes.length; i++) {
                const item = this.bboxes[i]
                // const catURL = '/production/description'
                // const catURL = 'https://50j0dal2y9.execute-api.ap-southeast-1.amazonaws.com/production/description'
                // const cat = await this.$axios.get(catURL + item.name)
                // const priceURL = '/production/price'
                // const priceURL = "https://50j0dal2y9.execute-api.ap-southeast-1.amazonaws.com/production/price"
                // const price = await this.$axios.get(priceURL + item.name)
                // item.under = cat
                // item.price = price
                item.under = `cat ${item.id}`
                item.price = 100 * (i+1)
            }
            console.log("After saving listings")
            console.log(this.bboxes)
            // this.items = newItems
            this.earnings = this.bboxes.map(b => b.price).reduce((a, b) => parseInt(a) + parseInt(b), 0);
            this.total = this.earnings
            this.updateEarnings()
        },
        updateItem() {
            // const index = this.items.map(function(i) { return i.id; }).indexOf(this.activeBox.id); // get active index
            const index = this.activeBox.id
            // this.bboxes[index].name = this.activeBox.name; // update the name
            console.log("Im here!")
            console.log(`itemName is ${this.itemName}`)
            this.bboxes[index].name = this.itemName; // update the name
            console.log(`which is stored as ${this.bboxes[index].name}`)
            // this.items[index].Category = this.activeBox.class;
            // this.items[index].list = this.list; // update listing bool
        },
        updateListing(item) {
            item.list ? this.bboxes[item.id].list = true : this.bboxes[item.id].list = false
            // this.bboxes[item.id].list = item.list
            console.log(`Switched listing ${item.name} to ${this.bboxes[item.id].list}`)
            // console.log("Upon switching....")
            // console.log(`Current changed: ${this.bboxes[item.id].list}, while the rest are ${this.bboxes}`)
            // this.earnings = this.bboxes.map(b => b.price).reduce((a, b) => a + b, 0);
            this.updateEarnings()
        },
        editListing() {
            this.edit = false
            this.updateEarnings()
        },
        updateEarnings() {
            this.earnings = this.bboxes.filter(b => b.list).map(e => e.price).reduce((a, b) => parseInt(a) + parseInt(b));
            const percent = this.earnings/this.total * 100
            console.log(`updateEarnings: Earnings is now ${this.earnings}`)
            console.log(`updateEarnings: Total is now ${this.total}`)
            console.log(`updateEarnings: Percent is now ${percent}`)
            this.chartOptions.plotOptions.radialBar.hollow.size = `Potential Earnings based on ${this.listedCount()} items selected`
            this.chartOptions.labels = [`$${this.earnings}`]
            this.series = [percent]
        },
        listedCount() {
            // const listed = this.items.filter(function (i) {
            const listed = this.bboxes.filter(b => b.list).filter(Boolean).length; // count number of listed items
            console.log(`Number of listed items: ${listed}`)
            return listed
        },
        listItems() {
            for(let b=0; b < this.bboxes.length; b++) {
                const item = this.bboxes[b]
                const data = new FormData();
                data.append('name', item.name);
                data.append('price', item.price);
                data.append('for_sale', item.list);
                data.append('images', [
                    {
                        'filename': this.filename // contains image data
                    }
                ]);
                // data.append('tags', );
                // data.append('description', '');

            }

            // await this.$axios.$post("/api/listings/create", data).then(res =>
            // {
            //     console.log("response for listings/create: ", res);
            // }).catch(error => {
            //     console.log("Failed!!!!")
            //     console.log(error)
            // })

            // const data = {
            //     "name": "string",
            //     "description": "string",
            //     "price": 0,
            //     "for_sale": true,
            //     "images": [
            //         {
            //         "filename": "string"
            //         }
            //     ],
            //     "tags": []
            // }
        }
    }
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

.btn {
    display: flex;
    justify-content: flex-end;
    padding: 20px;
}
 </style>
