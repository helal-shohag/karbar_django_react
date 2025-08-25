import {legacy_createStore as createStore,combineReducers,applyMiddleware} from 'redux'
import { productListReducers } from './reducers/ProductReducers'

import {thunk} from 'redux-thunk'
import {composeWithDevTools } from '@redux-devtools/extension'


const reducer = combineReducers({
    productListReducers:productListReducers,
})

const initialState = {}

const middleware  = [thunk]

const store = createStore(reducer,initialState,composeWithDevTools(applyMiddleware(...middleware)))


export default store