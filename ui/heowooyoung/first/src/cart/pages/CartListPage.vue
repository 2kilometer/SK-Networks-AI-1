<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title>Shopping Cart</v-card-title>
                    <v-card-text>
                        <v-table>
                            <thead>
                            <tr>
                                <th>Product</th>
                                <th>Price</th>
                                <th>Quantity</th>
                                <th>Total</th>
                                <th>Actions</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-for="item in cartItems" :key="item.id">
                                <td>{{ item.productName }}</td>
                                <td>{{ item.price }}</td>
                                <td>
                                    <v-text-field
                                            v-model="item.quantity"
                                            type="number"
                                            min="1"
                                            @change="updateQuantity(item)"
                                    ></v-text-field>
                                </td>
                                <td>{{ item.price * item.quantity }}</td>
                                <td>
                                    <v-btn color="red" @click="removeItem(item)">Remove</v-btn>
                                </td>
                            </tr>
                            </tbody>
                        </v-table>
                        <v-divider></v-divider>
                        <v-row>
                            <v-col>
                                <v-btn color="blue" @click="checkout">Checkout</v-btn>
                            </v-col>
                            <v-col class="text-right">
                                <strong>Total: {{ cartTotal }}</strong>
                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    data() {
        return {
            cartItems: [
                // 예시 데이터: 실제 데이터는 API 호출 등을 통해 받아올 수 있습니다.
                { id: 1, productName: "Product 1", price: 10.0, quantity: 1 },
                { id: 2, productName: "Product 2", price: 20.0, quantity: 2 },
            ],
        };
    },
    computed: {
        cartTotal() {
            return this.cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
        },
    },
    methods: {
        updateQuantity(item) {
            // 수량 업데이트 로직을 여기에 추가합니다.
        },
        removeItem(item) {
            this.cartItems = this.cartItems.filter(cartItem => cartItem.id !== item.id);
        },
        checkout() {
            // 체크아웃 로직을 여기에 추가합니다.
        },
    },
};
</script>

<style>
/* 필요한 스타일을 여기에 추가합니다. */
</style>