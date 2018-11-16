import React from 'react';
import { shallow } from 'enzyme';
import ExampleWorkModal from '../js/example-work-modal';

import Enzyme from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
Enzyme.configure({ adapter: new Adapter() });

describe("ExampleWorkModal component", () => {
  let component = shallow(<ExampleWorkModal />);
  expect("Hello").toEqual("Hello");
  
