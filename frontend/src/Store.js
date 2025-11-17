import {legacy_createStore as createStore,combineReducers,applyMiddleware} from 'redux'
import { productListReducers,productDetailReducers} from './reducers/ProductReducers'


import {thunk} from 'redux-thunk'
import {composeWithDevTools } from '@redux-devtools/extension'
import { cartReducer } from './reducers/CartReducer'

const reducer = combineReducers({
    productList : productListReducers,
    productDetail : productDetailReducers,
    cart: cartReducer,
})

const cartItemsFromStorage = localStorage.getItem('cartitems') ? JSON.parse(localStorage.getItem('cartitems')) : []


const initialState = {
    cart : {cartItems : cartItemsFromStorage}
}

const middleware  = [thunk]

const store = createStore(reducer,initialState,composeWithDevTools(applyMiddleware(...middleware)))

export default store