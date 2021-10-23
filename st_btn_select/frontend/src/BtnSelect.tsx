import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"

import './custom.css'

interface State {
  current: number | undefined
}

class MyComponent extends StreamlitComponentBase<State> {
  public state = { current: undefined }

  componentDidMount(): void {
    super.componentDidMount()
    document.body.style.background = 'transparent'
  }

  render(): ReactNode {
    // Arguments
    const options: string[] = this.props.args['options']
    const nav: boolean = this.props.args['nav']
    const defaultIndex: number = this.props.args['default']

    // Computed values
    const current: number = this.state.current ?? defaultIndex
    const Wrapper = nav ? 'nav' : 'div'
    const theme: string = this.props?.theme?.base ?? 'light'

    return (
      <Wrapper className="wrapper">
        {options.map((option, idx) => (
          <button
            onClick={() => this.onClicked(idx)}
            className={theme}
            disabled={idx === current}
            key={idx}
          >
            {option}
          </button>
        ))}
      </Wrapper>
    )
  }

  private onClicked = (idx: number): void => {
    this.setState(
      prevState => ({ current: idx }),
      () => Streamlit.setComponentValue(idx)
    )
  }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(MyComponent)
