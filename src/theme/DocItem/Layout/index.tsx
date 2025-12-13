import React from 'react';
import DocItemLayout from '@theme-original/DocItem/Layout';
import Chatbot from '@site/src/components/Chatbot';
import type {WrapperProps} from '@docusaurus/types';

type Props = WrapperProps<typeof DocItemLayout>;

export default function DocItemLayoutWrapper(props: Props): JSX.Element {
  return (
    <>
      <DocItemLayout {...props} />
      <Chatbot />
    </>
  );
}