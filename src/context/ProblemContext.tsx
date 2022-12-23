import { createContext, useContext, useState } from "react";

interface IContext {
  data: any;
  setData: any;
}

const Context = createContext<IContext>({} as IContext)

export function ContextProblem({ children }: any) {

  const [data, setData] = useState(null);

  return (
    <Context.Provider value={{
      data: data,
      setData: setData
    }}>
      {children}
    </Context.Provider>
  )
}

export function useContextProblem() {
  const value = useContext(Context)
  return value
}