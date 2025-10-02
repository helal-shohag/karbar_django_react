import React from 'react'
import { Link } from 'react-router-dom';
import {Form,Button,Col,Row} from 'react-bootstrap'
import FromContainer from '../components/FromContainer'

function Register() {
  const [email,setEmail] = React.useState('')
  const [password,setPassword] = React.useState('')

    const handleSubmit= (e) =>{
        e.preventDefault()
        console.log('submitted')
      }
          
  return (
    <FromContainer>
        <h2>Register</h2>
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId='email'>
            <Form.Label>Email Address</Form.Label>
            <Form.Control type='email' placeholder='Enter email' value={email} onChange={(e) => setEmail(e.target.value)} ></Form.Control>
          </Form.Group>

          <Form.Group controlId='email'>
            <Form.Label>Email Address</Form.Label>
            <Form.Control type='email' placeholder='Enter email' value={email} onChange={(e) => setEmail(e.target.value)} ></Form.Control>
          </Form.Group>

          <Form.Group controlId='email'>
            <Form.Label>Email Address</Form.Label>
            <Form.Control type='email' placeholder='Enter email' value={email} onChange={(e) => setEmail(e.target.value)} ></Form.Control>
          </Form.Group>

          <Form.Group controlId='password'>
            <Form.Label >Password</Form.Label>
            <Form.Control type='password' placeholder='Enter password' value={password} onChange={(e) => setPassword(e.target.value)} ></Form.Control>
          </Form.Group>
               <Row className='py-3'>
          <Col>
            Have an Account? <Link to='/login'>Login</Link>
          </Col>
         </Row>
         <Button type='submit' variant='primary' className='mt-4 mb-4' onClick={handleSubmit}>Submit</Button>
        </Form>
  
    </FromContainer>
  )
}

export default Register