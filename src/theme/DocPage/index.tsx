import React from 'react';
import DocPage from '@theme-original/DocPage';
import Chatbot from '@site/src/components/Chatbot';
import type {WrapperProps} from '@docusaurus/types';

type Props = WrapperProps<typeof DocPage>;

export default function DocPageWrapper(props: Props): JSX.Element {
  return (
    <>
      <DocPage {...props} />
      <Chatbot />
    </>
  );
}