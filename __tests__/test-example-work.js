import React from 'react';
import { shallow } from 'enzyme';
import ExampleWork from '../js/example-work';

import Enzyme from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
Enzyme.configure({ adapter: new Adapter() });

describe("ExampleWork component", () => {
  expect("Hello").toEqual("Hello");
