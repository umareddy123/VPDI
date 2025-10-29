/***************************************************************************
 * Copyright 1996-2025 Synopsys, Inc.
 *
 * This Synopsys software and all associated documentation are proprietary
 * to Synopsys, Inc. and may only be used pursuant to the terms and
 * conditions of a written license agreement with Synopsys, Inc.
 * All other use, reproduction, modification, or distribution of the
 * Synopsys software or the associated documentation is strictly prohibited.
 ***************************************************************************/
 

/***************************************************************************
 * Generated snippet, used for detecting user edits.
 * CHECKSUM:211e0e4d210c23d3fd413083f94554a2311a4c4d
 ***************************************************************************/
 
#pragma once

#include "RNS_MyModel1_U2ABase.h"


/**
 * \copydoc RNS_MyModel1_U2ABase
 */
class RNS_MyModel1_U2A : public RNS_MyModel1_U2ABase {
  public:
#if (defined SYSTEMC_VERSION && SYSTEMC_VERSION <= 20221128 /*2.3.4*/)
    SC_HAS_PROCESS(RNS_MyModel1_U2A);
#endif

    RNS_MyModel1_U2A(sc_core::sc_module_name name);

  private:
    friend class RNS_MyModel1_U2ACovermodel;

    
    
  private:
        
};

